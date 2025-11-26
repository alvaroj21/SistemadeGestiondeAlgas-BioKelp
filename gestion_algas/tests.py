"""
Tests para la aplicación de gestión de algas
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from decimal import Decimal
from .models import TipoAlga, RegistroProduccion, ControlAcceso

Usuario = get_user_model()


class UsuarioModelTest(TestCase):
    """Tests para el modelo Usuario"""
    
    def setUp(self):
        self.admin = Usuario.objects.create_user(
            username='admin_test',
            email='admin@test.cl',
            password='testpass123',
            first_name='Admin',
            last_name='Test',
            rol='admin'
        )
        self.trabajador = Usuario.objects.create_user(
            username='trabajador_test',
            email='trabajador@test.cl',
            password='testpass123',
            first_name='Trabajador',
            last_name='Test',
            rol='trabajador'
        )
    
    def test_crear_usuario(self):
        """Test de creación de usuario"""
        self.assertEqual(self.admin.username, 'admin_test')
        self.assertEqual(self.admin.rol, 'admin')
        self.assertTrue(self.admin.es_admin())
        self.assertFalse(self.trabajador.es_admin())
    
    def test_metodos_rol(self):
        """Test de métodos de rol"""
        self.assertTrue(self.admin.es_admin())
        self.assertFalse(self.admin.es_trabajador())
        self.assertTrue(self.trabajador.es_trabajador())
        self.assertFalse(self.trabajador.es_admin())


class TipoAlgaModelTest(TestCase):
    """Tests para el modelo TipoAlga"""
    
    def setUp(self):
        self.tipo_alga = TipoAlga.objects.create(
            nombre='Alga Test',
            factor_conversion=Decimal('1.50'),
            descripcion='Alga de prueba',
            activo=True
        )
    
    def test_crear_tipo_alga(self):
        """Test de creación de tipo de alga"""
        self.assertEqual(self.tipo_alga.nombre, 'Alga Test')
        self.assertEqual(self.tipo_alga.factor_conversion, Decimal('1.50'))
        self.assertTrue(self.tipo_alga.activo)
    
    def test_str_representation(self):
        """Test de representación en string"""
        self.assertEqual(str(self.tipo_alga), 'Alga Test')


class RegistroProduccionModelTest(TestCase):
    """Tests para el modelo RegistroProduccion"""
    
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username='test_user',
            email='test@test.cl',
            password='testpass123',
            first_name='Test',
            last_name='User',
            rol='trabajador'
        )
        self.tipo_alga = TipoAlga.objects.create(
            nombre='Alga Test',
            factor_conversion=Decimal('2.00')
        )
        self.registro = RegistroProduccion.objects.create(
            usuario=self.usuario,
            tipo_alga=self.tipo_alga,
            cantidad_cosechada=Decimal('100.00'),
            sector='Sector Norte'
        )
    
    def test_crear_registro(self):
        """Test de creación de registro de producción"""
        self.assertEqual(self.registro.cantidad_cosechada, Decimal('100.00'))
        self.assertEqual(self.registro.sector, 'Sector Norte')
    
    def test_cantidad_con_factor(self):
        """Test de cálculo con factor de conversión"""
        cantidad_esperada = Decimal('100.00') * Decimal('2.00')
        self.assertEqual(self.registro.cantidad_con_factor, cantidad_esperada)


class LoginViewTest(TestCase):
    """Tests para la vista de login"""
    
    def setUp(self):
        self.client = Client()
        self.usuario = Usuario.objects.create_user(
            username='testuser',
            email='test@test.cl',
            password='testpass123',
            first_name='Test',
            last_name='User',
            rol='trabajador'
        )
        self.login_url = reverse('login')
    
    def test_login_page_status_code(self):
        """Test de acceso a página de login"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion_algas/login.html')
    
    def test_login_exitoso(self):
        """Test de login exitoso"""
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
    
    def test_login_fallido(self):
        """Test de login con credenciales incorrectas"""
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)


class DashboardViewTest(TestCase):
    """Tests para la vista del dashboard"""
    
    def setUp(self):
        self.client = Client()
        self.usuario = Usuario.objects.create_user(
            username='testuser',
            email='test@test.cl',
            password='testpass123',
            first_name='Test',
            last_name='User',
            rol='trabajador'
        )
        self.dashboard_url = reverse('dashboard')
    
    def test_dashboard_sin_autenticacion(self):
        """Test de acceso al dashboard sin autenticación"""
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 302)  # Redirect a login
    
    def test_dashboard_con_autenticacion(self):
        """Test de acceso al dashboard con autenticación"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion_algas/dashboard.html')


class RegistroProduccionViewTest(TestCase):
    """Tests para la vista de registro de producción"""
    
    def setUp(self):
        self.client = Client()
        self.trabajador = Usuario.objects.create_user(
            username='trabajador',
            email='trabajador@test.cl',
            password='testpass123',
            first_name='Trabajador',
            last_name='Test',
            rol='trabajador'
        )
        self.tipo_alga = TipoAlga.objects.create(
            nombre='Alga Test',
            factor_conversion=Decimal('1.00'),
            activo=True
        )
        self.registro_url = reverse('registro_produccion')
    
    def test_crear_registro_produccion(self):
        """Test de creación de registro de producción"""
        self.client.login(username='trabajador', password='testpass123')
        response = self.client.post(self.registro_url, {
            'tipo_alga': self.tipo_alga.id,
            'cantidad_cosechada': '150.50',
            'sector': 'Sector Sur',
            'observaciones': 'Registro de prueba'
        })
        self.assertEqual(response.status_code, 302)  # Redirect después de crear
        self.assertEqual(RegistroProduccion.objects.count(), 1)


class UsuariosViewTest(TestCase):
    """Tests para la vista de gestión de usuarios"""
    
    def setUp(self):
        self.client = Client()
        self.admin = Usuario.objects.create_user(
            username='admin',
            email='admin@test.cl',
            password='testpass123',
            first_name='Admin',
            last_name='Test',
            rol='admin'
        )
        self.usuarios_url = reverse('usuarios')
    
    def test_acceso_solo_admin(self):
        """Test de acceso restringido solo a administradores"""
        trabajador = Usuario.objects.create_user(
            username='trabajador',
            password='testpass123',
            rol='trabajador'
        )
        self.client.login(username='trabajador', password='testpass123')
        response = self.client.get(self.usuarios_url)
        # Debe ser redirigido o recibir 403
        self.assertNotEqual(response.status_code, 200)
    
    def test_admin_puede_acceder(self):
        """Test de que admin puede acceder"""
        self.client.login(username='admin', password='testpass123')
        response = self.client.get(self.usuarios_url)
        self.assertEqual(response.status_code, 200)


class ControlAccesoModelTest(TestCase):
    """Tests para el modelo de control de accesos"""
    
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username='testuser',
            email='test@test.cl',
            password='testpass123'
        )
    
    def test_crear_control_acceso(self):
        """Test de creación de registro de acceso"""
        acceso = ControlAcceso.objects.create(
            usuario=self.usuario,
            ip_origen='127.0.0.1',
            tipo_acceso='login_exitoso'
        )
        self.assertEqual(acceso.usuario, self.usuario)
        self.assertEqual(acceso.tipo_acceso, 'login_exitoso')
        self.assertIsNotNone(acceso.fecha_acceso)
