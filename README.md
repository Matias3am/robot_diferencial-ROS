# SIMULACIÓN DE ROBOT DIFERENCIAL 4 RUEDAS CON ROS E INTEGRACIÓN SENSOR LIDAR

![](https://github.com/Matias3am/robot_diferencial-ROS/blob/main/proyecto2_ros/compilacion_robot/Imagenes/Imagenes/Captura%20desde%202024-07-15%2018-43-10.png)

# Aclaración 

En un principio estaba la intención de hacer un robot diferencial de 2 ruedas + 1 auxiliar junto con un griper en algun frente,
pero no pudimos ejecutar bien el asunto del griper asi que cambiamos el modelo a un diferencial de 4 ruedas + camara y sensor lidar


## _**REQUISITOS MÍNIMOS GENERALES**_ 
* Python
* ROS2 / IRON
* RVIZ
* Gazebo 

Los paquetes utilizados para este proyecto son los siguientes: 
```
sudo apt install ros-iron-xacro
sudo apt install ros-iron-gazebo-ros-pkgs
sudo apt-get install gedit
sudo apt install ros-iron-joint-state-publisher
sudo apt install ros-iron-joint-state-publisher-gui
sudo apt install ros-iron-core
sudo apt install ros-iron-ros-core
sudo apt install ros-iron-geometry2
sudo apt-get install ros-iron-gazebo-msgs
sudo apt-get install ros-iron-gazebo-plugins
sudo apt-get install ros-iron-ros-ign-bridge
sudo apt-get install ros-iron-teleop-twist-keyboard
```

# Estructura de los archivos

* **launch:** Aquí se encuentran los launchers necesarios para ejecutar los programas de rviz y gazebo con el modelo del robot de forma directa.
  * **display_launch.py:** Este archivo despliega solamente el ambiente rviz para visualizar el robot
  * **gazebo_launch.py:** Este archivo despliega el entorno de Gazebo junto con el de Rviz al mismo tiempo. 
* **rviz:** Aquí se almacena la configuración de rviz para que al abrirse se visualice tanto la cámara como lo que detecta el sensor lidar.
* **urdf:** Aquí se encuentran los archivos que describen la estructura del robot:
  * **camara.urdf:** Este archivo corresponde al módelo y funcionalidad de la cámara del robot ubicado en uno de los frontales de este mismo.
  * **lidar.urdf:** Este archivo corresponde al módelo y funcionalidad del sensor lidar ubicado al centro superior del robot.
  * **propiedades_xacro.urdf:** En este archivo están las propiedades/variables xacro del robot y un módelo base para definir la inercia de algunos componentes.
  * **robotin.urdf:** Este archivo es el modelo inicial del robot sin xacros.
  * **robotin_xacro.urdf:** Este archivo corresponde al modelo base del robot pero con xacros.
  * **ruedas_xacro.urdf:** Este archivo define la estructura y comportamiento de las ruedas.

# _**¿ Como compilar las simulaciones ?**_ 
Para compilar el programa se necesitarán 2 ventanas de terminal: Una para Gazebo & Rviz y una para el control por teclado. 

Para la terminal que abrirá Gazebo y Rviz se necesitan incluir estas lineas de código primero: 
```
source /opt/ros/iron/setup.bash
colcon build --packages-select compilacion_robot
source install/setup.bash
```

# _**GAZEBO & RVIZ**_
Una vez inicializados los comandos que se dictaron anteriormente, se utiliza el siguiente comando para abrir tanto la simulación de Gazebo, como la de Rviz: 
```
ros2 launch compilacion_robot  gazebo_launch.py
```
Si el programa cargó correctamente, debería verse como la siguiente imagen:
![](https://github.com/Matias3am/robot_diferencial-ROS/blob/main/proyecto2_ros/compilacion_robot/Imagenes/Imagenes/Captura%20desde%202024-07-15%2018-41-11.png)

Ya con la simulación de Gazebo andando se procede a insertar el mapa, el cual se encontrará en la carpeta **"casita"** en la posición que uno desee, hecho esto debería verse así:

![](https://github.com/Matias3am/robot_diferencial-ROS/blob/main/proyecto2_ros/compilacion_robot/Imagenes/Imagenes/Captura%20desde%202024-07-15%2018-45-01.png)

En paralelo se debería abrir una ventana de Rviz la cual debería verse como la imagen de abajo, en donde en la esquina inferior izquierda se puede observar lo que está visualizando la cámara del robot
y en el mapa se pueden observar las estructuras detectadas por el sensor lidar:
![](https://github.com/Matias3am/robot_diferencial-ROS/blob/main/proyecto2_ros/compilacion_robot/Imagenes/Imagenes/Captura%20desde%202024-07-15%2018-45-21.png)

# **_Teleoperación_**
Llegados a este punto lo único que quedaria pendiente es el poder controlar el movimiento del robot, para eso se necesitan ejecutar estos 2 comandos en una ventana aparte de la que se utilizó para ejecutar el Gazebo/Rviz: 
```
source /opt/ros/iron/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
La terminal debería entregar algo así: 
```
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
anything else : stop

CTRL-C to quit
```
Como el robot es del tipo diferencial, al presionar las teclas "i" este avanzará hacia adelante y las teclas "j" y "l" haran rotar el robot en dirección izquierda o derecha, para detener el robot se presiona la tecla "k"
## Solamente te queda explorar y probar el robot :)  

Aquí algunos tests que realizamos:

![](https://github.com/Matias3am/robot_diferencial-ROS/blob/main/proyecto2_ros/compilacion_robot/Imagenes/Imagenes/Captura%20desde%202024-07-15%2018-41-50.png)

![](https://github.com/Matias3am/robot_diferencial-ROS/blob/main/proyecto2_ros/compilacion_robot/Imagenes/Imagenes/Captura%20desde%202024-07-15%2018-43-47.png)
