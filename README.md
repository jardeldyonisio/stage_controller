# Stage Controller

A atividade consiste em desenvolver um nodo ROS para controlar um robô diferencial. Foi implementado um nodo capaz de guiar o robô até uma coordenada alvo no plano sem colidir com os obstáculo do cenário, usando sensor laser.

## Simulation Quick Start

### Dependências

- Ubuntu
- [ROS Noetic]([https://github.com/butia-bots/butia_learning/wiki/Instala%C3%A7%C3%B5es-importantes#ros-robot-operating-system](http://wiki.ros.org/noetic/Installation/Ubuntu))

### Preparando ambiente

Após instalar as dependências, é necessário criar um workspace para testar o pacote, para isso, rode o comando abaixo:

```
mkdir -p ~/furg_ws/src
```

Acesse a pasta com o seguinte comando:
```
cd ~/butia_ws/src
```

Clone this repository using the following command:

```
git clone https://github.com/jardeldyonisio/stage_controller.git
```

Para compilar o pacote, acesse o workspace com o comando:

```
cd ~/furg_ws/
```
Compile o pacote:

```
catkin_make
```

### Como executar

Inicialmente, acesse o seu workspace:

```
cd ~/furg_ws/
```

Execute o comando source, opções em bash e zsh:

```
source devel/setup.bash
```
ou:
```
source devel/setup.zsh
```
Rode o launch:
```
roslaunch stage_controller launcher.launch
```
### Simulação

Ao rodar o launch, irá abrir uma janela com o simulador executando.

![Screenshot from 2023-05-25 11-46-33](https://github.com/jardeldyonisio/stage_controller/assets/6722220/30af8b9a-f512-4f3c-93cf-d58761dae9e6)

Vídeo: https://youtu.be/l2s3l7QXYus
