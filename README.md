# BarberManager

Sistema de gestión integral para barberías que permite administrar citas, ventas de productos, barberos y generar reportes.

## Descripción

BarberManager es una aplicación web desarrollada con Flask que proporciona una solución completa para la gestión de barberías. El sistema permite a los clientes reservar citas, a los administradores gestionar el personal, inventario de productos y ventas, además de generar reportes de operación.

## Características Principales

- 🗓️ Gestión de citas y reservaciones
- 💈 Administración de barberos
- 🏪 Inventario y venta de productos
- 💰 Sistema de pagos (efectivo/tarjeta)
- 📊 Generación de reportes
- 👤 Gestión de usuarios y roles
- 🛍️ Tienda en línea de productos

## Estructura del Proyecto

```
BarberManager/
├── main.py                 # Archivo principal de la aplicación Flask
├── backup-barberManager.sql # Respaldo de la base de datos
├── models/                 # Modelos de datos
│   ├── producto_model.py
│   └── ...
├── helpers/               # Funciones auxiliares y conexión a BD
│   ├── conection.py
│   ├── producto.py
│   └── ...
├── templates/             # Plantillas HTML
│   ├── index.html
│   ├── AdminManager.html
│   ├── productos.html
│   └── ...
├── static/               # Archivos estáticos
│   ├── images/
│   ├── js/
│   └── styles/
└── sql/                  # Scripts SQL y migraciones
```

## Requisitos Técnicos

### Dependencias Principales
- Python 3.8+
- Flask
- MySQL
- mysql-connector-python
- Bootstrap 5.3.0
- Font Awesome 6.4.0

### Base de Datos
- MySQL 8.0+
- Esquema definido en `backup-barberManager.sql`

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/BarberManager.git
cd BarberManager
```

2. Crear un entorno virtual e instalar dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configurar la base de datos:
```bash
mysql -u root -p < backup-barberManager.sql
```

4. Iniciar la aplicación:
```bash
python main.py
```

## Uso

### Panel de Administración
- Acceder a `/adminManager` para gestionar citas
- Acceder a `/productos` para gestionar inventario
- Acceder a `/reportes` para ver reportes de ventas

### Portal del Cliente
- Página principal en `/` para ver servicios y productos
- Reservar citas desde la sección "Reservar"
- Comprar productos desde la tienda en línea

## Características de Seguridad
- Autenticación de usuarios
- Roles y permisos
- Protección de rutas administrativas
- Validación de formularios
- Sanitización de datos

## Contribución
1. Fork el proyecto
2. Cree una rama para su característica (`git checkout -b feature/AmazingFeature`)
3. Commit sus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abra un Pull Request

## Licencia
Este proyecto está bajo la Licencia MIT - vea el archivo `LICENSE` para más detalles.

## Contacto
Link del Proyecto: [https://github.com/tu-usuario/BarberManager](https://github.com/tu-usuario/BarberManager) 