# tfc-drones

## 1. representação de objetos (fazer 25.4.2022)

#### 1. Criar os seguintes classes/objetos no [models](https://github.com/ulht-drones/tfc-drones/blob/main/drones/models.py):
   1. cenário, com os campo:
      * nome
      * coordenada_centro - JSONField
   2. drone, com  os campos: 
      * nome
      * posicao - JSONField
      * frequencia - integerfield
      * potencia transmitida - integerfield
      * antena - forneign key
      * cenario - ForeignKey.
   3. célula, com  os campos: 
      * nome
      * posicao - JSONField
      * antena - forneign key
      * cenario - ForeignKey.
   4. antena com campos: 
      * frequencia - integerfield
      * potencia transmitida - integerfield
      * tilt - integerfield
      * azimute - integerfield
      * nome
      * ganho
      * ficheiro - FileField
      * diagrama_vertical - imageField
      * diagrama_horizontal - imageField
      * heatmap - imageField 
   5. polígono da área de serviço, com os campos: 
      * nome
      * pontos, JSonField (com coordenadas dos vertices do poligono). 

#### 2. No  adminC, criar objetos de cada tipo. 

* usar como cenário a universidade da Sérvia. 
* representar posicao das celulas e drone nessa zona. Formato de coordenada:
    
    ```jsone
    {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [-9.204356, 38.698116]}}
                      
    ```
    
* usar para já em todas as celulas e drone a mesma antena:
    * [ficheiro](https://github.com/ulht-drones/tfc-drones/blob/main/dados/antenna_diagrams/80010504_1750_x_co_m45_00t.msi),
    * [vertical](https://github.com/ulht-drones/tfc-drones/blob/main/dados/antenna_diagrams/80010504_1750_x_co_m45_00t_vertical.png) 
    * [horizontal](https://github.com/ulht-drones/tfc-drones/blob/main/dados/antenna_diagrams/80010504_1750_x_co_m45_00t_horizontal.png). 
        * Estes podem ser criados com a função [aqui](https://github.com/ulht-drones/tfc-drones/tree/main/dados/antenna_diagrams)), mas trataremos disso mais tarde.
    * [heatmap](https://github.com/ulht-drones/tfc-drones/blob/main/dados/heatmaps/heatmap.png). um heatmap ilustra como a antena do drone está a iluminar a área de serviço.

* poligono centrado no campo de futebol. ir buscar coordenadas de pontos que permitam construir um poligono em torno do estado. Formato do poligono (primeiro e ultimo ponto convem serem o mesmo, para "fechar" área polígono):
  
      ```json
         {
             'type': 'Feature',
             'geometry': {
                 'type': 'Polygon',
                 'coordinates': [
                     [
                         [-9.203356, 38.697116],
                         [-9.205356, 38.697116],
                         [-9.205356, 38.699116],
                         [-9.203356, 38.699116],
                         [-9.203356, 38.697116],
                     ]
                 ]
             }
         }
      ```



#### 3. na função [views](https://github.com/ulht-drones/tfc-drones/blob/16c1dfac3a7da4c0d3495ab19659ce3599c8cb04/drones/views.py#L12) ir buscar, alem das antenas, restantes objetos (drone, poligono, centro), e envia-los (no context) para o HTML. 

#### 4. Inserir, no mapa, no HTML os objetos (ver como fizemos para os pontos). imagem do heatmap deve usar as coordenadas do drone devem ser tais que heatmap deve estar sobreposta por cima do poligono (heatmap ilustra como a antena do drone está a iluminar a área de serviço).

#### 5. incluir no relatório esta informação, sobretudo visualização dos 4 tipos de objetos


## 2. visualizar info

* criar, no layout, ao lado direito uma caixa menu para visualiza:
   * info de célula (tabela com parametros e valores)
   * diagramas 
   * heatmap. 
* Deve haver um formulario permite escolher a celula, mostrando info da sua antena. usar um `fetch()`, comunicação assincrona AJAX (ver [aula de Programação Web](https://educast.fccn.pt/vod/clips/19qwlm80te/html5.html?locale=en) que explica).
* o heatmap deverá ser mostrado no mapa. a resntante informação numa caixa de informação ao lado direito, que pode ser minimizada se o utilizador quiser.

## 3. desenho de polígono pelo utilizador atraves de cliques no mapa

* ver este exemplo: https://docs.mapbox.com/mapbox-gl-js/example/mapbox-gl-draw/
* implementar a funcionalidade de desenho de um polígono sobre o mapa. 
   * deve haver opção "desenhar poligono"
   * utilizador deve poder desenhar um poligono na aplicação, clicando em pontos por forma a definir a área
   * a informação deve ser submetida e guardada na base de dados.
   * deve ser possivel apagar um poligono

## 4. dados reais
* usar os dados da Sérvia, coordenadas de celulas existentes. Atenção, que várias células podem estar "co-localizadas" no mesmo site (sitio), pois teem antenas a apontar para direções diferentes, ou usam frequencias diferentes


## 5. Desenho de antenas - para já não é necessário
* Experimentar [jupyter](https://github.com/ulht-drones/tfc-drones/blob/main/dados/antenna_diagrams/Desenho%20de%20diagramas%20de%20radia%C3%A7%C3%A3o%20duma%20antena.ipynb). Esta função recebe o nome de um ficheiro que tem o diagrama de radiação (ficheiro .msi) e cria pngs com diagramas de radiação vertical e horizontal da antena.
* usar a função (mesmo codigo) em [functions.py](https://github.com/ulht-drones/tfc-drones/blob/main/dados/antenna_diagrams/functions.py) para criar pngs dos diagramas vertical e horizontal. 

