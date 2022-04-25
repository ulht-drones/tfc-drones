# tfc-drones

## 1. representação de objetos (fazer 25.4.2022)

1. Criar os seguintes classes/objetos no models:
   1. centro do mapa
   2. drone, com  os campos: nome, posicao - JSONField, a) frequencia - integerfield, b) potencia transmitida - integerfield, c) antena - forneign key.
   3. célula, com  os campos: nome, posicao - JSONField,  a) frequencia - integerfield, b) potencia transmitida - integerfield, c) antena - forneign key.
   4. antena com campos: nome, ganho, ficheiro .msi que contem diagrama, desenho diagramas vertical e horizontal - imageField (ver exemplos [aqui](https://github.com/ulht-drones/tfc-drones/tree/main/dados/antenna_diagrams)) , heatmap (imageField).
      * um heatmap ilustra como a antena do drone está a iluminar a área de serviço
   5. polígono da área de serviço: nome e json com coordenadas dos vertices do poligono, e determinada cor. ver como defini o [poligono aqui](https://github.com/ulht-drones/tfc-drones/blob/b3936021d126f458109bffd9b9c1eff1963758d6/drones/templates/drones/mapa.html).

2. Criar objetos no admin de cada tipo. 
* centrar mapa na universidade da Sérvia. 
* representar posicao das celulas e drone nessa zona.
* inventar polígono em volta do estadio de futebol
* criar antena de drone, que usa como heatmap [esta imagem](https://github.com/ulht-drones/tfc-drones/blob/main/dados/heatmaps/heatmap.png)

3. na função view ir buscar esses objetos e envia-los no context para o HTML

4. Inserir, no mapa, no HTML os objetos. imagem do heatmap deve usar as coordenadas do drone devem ser tais que heatmap deve estar sobreposta por cima do poligono (heatmap ilustra como a antena do drone está a iluminar a área de serviço).

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
