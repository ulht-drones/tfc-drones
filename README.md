# tfc-drones

## 1. representação de objetos (fazer 25.4.2022)

1. Criar os seguintes classes/objetos no [models](https://github.com/ulht-drones/tfc-drones/blob/main/drones/models.py):
   1. centro do mapa
   2. drone, com  os campos: nome, posicao - JSONField, a) frequencia - integerfield, b) potencia transmitida - integerfield, c) antena - forneign key.
   3. célula, com  os campos: nome, posicao - JSONField,  a) frequencia - integerfield, b) potencia transmitida - integerfield, c) antena - forneign key.
   4. antena com campos: nome, ganho, ficheiro - FileField, diagrama_vertical - imageField, diagrama_horizontal - imageField, heatmap - imageField 
   5. polígono da área de serviço: nome e json com coordenadas dos vertices do poligono, e determinada cor. 

2. Criar objetos no admin de cada tipo. 
* centrar mapa na universidade da Sérvia. 
* representar posicao das celulas e drone nessa zona.
* inventar polígono em volta do estadio de futebol
* usar para já em todas as antenas os seguintes diagramas: [vertical](https://github.com/ulht-drones/tfc-drones/blob/main/dados/antenna_diagrams/80010504_1750_x_co_m45_00t_vertical.png) e [horizontal](https://github.com/ulht-drones/tfc-drones/blob/main/dados/antenna_diagrams/80010504_1750_x_co_m45_00t_horizontal.png). Estes podem ser criados com a função [aqui](https://github.com/ulht-drones/tfc-drones/tree/main/dados/antenna_diagrams)), mas trataremos disso mais tarde.
      * um heatmap ilustra como a antena do drone está a iluminar a área de serviço. para já, associar a todas as antenas [esta imagem](https://github.com/ulht-drones/tfc-drones/blob/main/dados/heatmaps/heatmap.png) em todos
      * ficheiro guarda um ficheiro .msi que contem descrição do diagrama. para já, associar a todas as antenas [este ficheiro](https://github.com/ulht-drones/tfc-drones/blob/main/dados/antenna_diagrams/80010504_1750_x_co_m45_00t.msi) 
      * nome da antena é nome do ficheiro .msi anterior
* poligono centrado no campo de futebol, ver como defini um [poligono aqui](https://github.com/ulht-drones/tfc-drones/blob/16c1dfac3a7da4c0d3495ab19659ce3599c8cb04/drones/templates/drones/mapa.html#L48). ir buscar coordenadas de pontos que permitam construir um poligono em torno do estado

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



3. na função [views](https://github.com/ulht-drones/tfc-drones/blob/16c1dfac3a7da4c0d3495ab19659ce3599c8cb04/drones/views.py#L12) ir buscar, alem das antenas, restantes objetos (drone, poligono, centro), e envia-los (no context) para o HTML. 

4. Inserir, no mapa, no HTML os objetos (ver como fizemos para os pontos). imagem do heatmap deve usar as coordenadas do drone devem ser tais que heatmap deve estar sobreposta por cima do poligono (heatmap ilustra como a antena do drone está a iluminar a área de serviço).

5. incluir no relatório esta informação, sobretudo visualização dos 4 tipos de objetos


## 2. visualizar diagramas de radiação

* Experimentar [jupyter](https://github.com/ulht-drones/tfc-drones/blob/main/dados/antenna_diagrams/Desenho%20de%20diagramas%20de%20radia%C3%A7%C3%A3o%20duma%20antena.ipynb). Esta função recebe o nome de um ficheiro que tem o diagrama de radiação (ficheiro .msi) e cria pngs com diagramas de radiação vertical e horizontal da antena.
* usar a função (mesmo codigo) em [functions.py](https://github.com/ulht-drones/tfc-drones/blob/main/dados/antenna_diagrams/functions.py) para criar pngs dos diagramas vertical e horizontal. 
* guardar como imagem cada um dos diagramas
* criar, no layout, uma caixa ao lado direito para visualizar os diagramas. Deve haver um formulario com elemento select que permite escolher a celula que queremos ver o diagrama. usar um `fetch()`, comunicação assincrona AJAX (ver [aula de Programação Web](https://educast.fccn.pt/vod/clips/19qwlm80te/html5.html?locale=en) que explica).


## 3. desenho de polígono
* ver este exemplo: https://docs.mapbox.com/mapbox-gl-js/example/mapbox-gl-draw/
* implementar a funcionalidade de desenho de um polígono sobre o mapa
* a informação deve ser submetida e guardada na base de dados.

## 4. dados reais
* usar os dados da Sérvia, coordenadas de celulas existentes. Atenção, que várias células podem estar "co-localizadas" no mesmo site (sitio), pois teem antenas a apontar para direções diferentes, ou usam frequencias diferentes
