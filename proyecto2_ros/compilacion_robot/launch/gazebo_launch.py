# Importamos los módulos necesarios para el lanzamiento y las sustituciones de launch.
import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

# Definimos una función que genera la descripción del lanzamiento.
def generate_launch_description():
    # Encuentra la ruta del paquete 'compilacion_robot'.
    pkg_share = launch_ros.substitutions.FindPackageShare(package='compilacion_robot').find('compilacion_robot')
    # Define la ruta predeterminada del archivo URDF del robot.
    default_model_path = os.path.join(pkg_share, 'urdf/robotin_xacro.urdf')

    # Define el nodo robot_state_publisher para publicar el estado del robot.
    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher', # El paquete que contiene el ejecutable.
        executable='robot_state_publisher', # El ejecutable que se va a lanzar.
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}] # Parámetros del nodo.
    )

    # Define el nodo joint_state_publisher para publicar el estado de las articulaciones del robot.
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',  # El paquete que contiene el ejecutable.
        executable='joint_state_publisher',  # El ejecutable que se va a lanzar.
        name='joint_state_publisher' # Nombre del nodo.
    )
    
    # Define el nodo spawn_entity para agregar el robot en el simulador Gazebo.
    spawn_entity = launch_ros.actions.Node(
    package='gazebo_ros', # El paquete que contiene el ejecutable.
    executable='spawn_entity.py', # El ejecutable que se va a lanzar.
    arguments=['-entity', 'robotin', '-topic', 'robot_description'], # Argumentos para el nodo.
    output='screen' # La salida se mostrará en la pantalla.
    )
    
    # Retorna una descripción del lanzamiento con los nodos y procesos declarados.
    return launch.LaunchDescription([
        # Declara un argumento de lanzamiento para la ruta del modelo.
        launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                            description='Absolute path to robot urdf file'),
        # Ejecuta el proceso de lanzamiento de Gazebo con los plugins de ROS.
        launch.actions.ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'], output='screen'),
        # Incluye el nodo joint_state_publisher en la descripción del lanzamiento.
        joint_state_publisher_node,
        # Incluye el nodo robot_state_publisher en la descripción del lanzamiento.
        robot_state_publisher_node,
        # Incluye el nodo spawn_entity en la descripción del lanzamiento.
        spawn_entity,
    ])
