Projeto "Bate-Bate", baseado no famoso display de “DVD” que quando batia em qualquer direção, trocava de cor aleatoriamente.

Este projeto possui 3 partes, a Mecânica de Movimentos, Game e Main. Cada um desses elementos possui seus respectivos "Atributos" e "Métodos".

1 - Classe MovText: Aqui serão declaradas as lógicas, variáveis e definições, sendo responsável pela largura e altura da janela, o movimento do texto, e a lógica de como o texto se comporta conforme ele vai batendo nas bordas, trocando de cor aleatoriamente.

2 - Classe Game: Aqui serão declarados o construtor e o tempo do jogo, sendo que o construtor é responsável por iniciar todos os atributos da classe, e o tempo manipula e controla a taxa de quadros do jogo.

3 - Classe Main: Essa classe inicia o jogo, importando a classe Game, e pega as suas características, rodando o método run, que executa o jogo.

------------------------------------------------------

<h1>Estrutura do Diagrama.<h1>

<div align=center>

<img height="200em" src="./img/diagrama-uml.png.png">

</div>

------------------------------------------------------

------------------------------------------------------

<h1>Classe Movendo Texto (arquivo: mecmov.py) (classe: MovText).<h1>

<div align=center>

<h3>Atributos.</h3>

<p>self.fonte: Define o tipo de texto, o tamanho da fonte do texto e o estilo visual que vai aparecer para o usuário.</p>

<p>self.texto: Define o texto que será exibido na tela do jogo.</p>

<p>self.altura: Define a altura da janela do jogo.</p>

<p>self.largura: Define a largura da janela do jogo</p>

<p>self.texto_surf: Define a superfície que ver o texto renderizado.</p>

<p>self.rect: Define a área em que o texto aparecerá, em forma de um retângulo.</p>

<p>self.velocidade_x: Define a velocidade horizontal do jogo.</p>

<p>self.velocidade_y: Define a velocidade vertical do jogo.</p>

<h3>Métodos.</h3>

<p>__init__: Este é o construtor da classe (MovText), onde ele inicia todos os atributos da mesma.</p>

<p>gerar_numero_nao_zero: Este método gera numeros que não sejam 0, e nulos, entre os números -1 e 1.</p>

<p>move: Método usado para mover o texto na tela, e quando ele (texto), toca qualquer uma das bordas, ele troca de cor de forma aleatória.</p>

<p>change_color: Este elemento faz o texto trocar de cor de forma aleatória, conforme e bate nas bordas da janela.</p>

</div>

------------------------------------------------------

------------------------------------------------------

<h1>Classe Game (arquivo: game.py) (classe: Game).<h1>

<div align=center>

<h3>Atributos.</h3>

<p>self.largura: Define a largura da janela do jogo, que foi determinada com 800 pixels.</p>

<p>self.altura: Define a altura da janela do jogo, que foi determinada com 600 pixels.</p>

<p>self.tela: Define a criação da tela com a configurações especificadas, com 600 de altura e 800 de largura.</p>

<p>self.clock: Cria um objeto que é responsável por controlar e limitar a taxa de quadros do jogo.</p>

<p>self.MovText: Cria um objeto da classe (MovText) e passa as características da classe para o objeto criado.</p>

<h3>Métodos.</h3>

<p>__init__: Este é o construtor da classe (Game), onde ele inicia todos os atributos da mesma.</p>

<p>run: Este método executa o jogo, aplicando a lógica que foi declarada.</p>

</div>

------------------------------------------------------

------------------------------------------------------

<h1>Classe Main (arquivo: main.py) (classe: Main).<h1>

<div align=center>

<h3>Atributos.</h3>

<p>Game: Classe importada do arquivo (game.py), usada para iniciar o jogo.</p>

<h3>Métodos.</h3>

<p>__name__: Este método executa o run da classe Game, e então o jogo começa.</p>

</div>

------------------------------------------------------

------------------------------------------------------

Thank you so much for reading, have a nice day! :D

------------------------------------------------------