## Tutorial

- Baixar a imagem docker com mininet
    sudo docker pull iwaseyusuke/mininet

- Iniciar um novo container
    sudo docker run -it --privileged -e DISPLAY \
             -v /tmp/.X11-unix:/tmp/.X11-unix \
             -v /lib/modules:/lib/modules \
             iwaseyusuke/mininet

- Dentro do container
    apt-get update
    apt-get upgrade
    apt-get install nano

- visualizar containers abertos e fechados
    sudo docker ps -a

- Iniciar container
    Sudo docker start `nome do container`


- Acessar container que foi fechado
    sudo docker attach happy_raman