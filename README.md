# tfc-drones

## representação de objetos (fazer 25.4.2022)

1. Criar os seguintes classes/objetos no models:
   * centro do mapa
   * drone (incluir como campos tambem a) frequencia - integerfield, b) potencia transmitida - integerfield, c) diagrama de radiação - charfield.
   * célula (incluir como campos tambem a) frequencia - integerfield, b) potencia transmitida - integerfield, c) diagrama de radiação - charfield.
   * polígono da área de serviço: nome e json com coordenadas dos vertices do poligono, e determinada cor. ver como defini o poligono em 
   * heatmap da zona iluminada pelo drone. usa para já a imagem em baixo. representa-a sobre o mapa com a propriedade "opacity: 0.5", por forma a que tenha transparencia que permita visualizar o mapa

2. Criar objetos no admin de cada tipo. 
* centrar mapa na universidade da Sérvia. 
* representar celulas e drone nessa zona.
* inventar polígono em volta do estadio de futebol
* sobrepor imagem sdo heatmap por cima do poligono

3. na função view ir buscar esses objetos e envia-los no context para o HTML

4. Inserir no mapa no HTML os objetos

5. incluir no relatório esta informação, sobretudo visualização dos 4 tipos de objetos

   
heatmap:

![heatmap](https://user-images.githubusercontent.com/42048382/165084159-6e416fad-fd9c-4491-8660-98c6e869e3ef.png)


## criar desenho dos diagramas de radiação
* usar a função em functions.py para criar pngs dos diagramas vertical e horizontal
* guardar como imagem cada um dos diagramas
* criar interface que permita ativar ou desativar visualização dos diagramas


## desenho de polígono
* ver este exemplo: https://docs.mapbox.com/mapbox-gl-js/example/mapbox-gl-draw/
* implementar a funcionalidade de desenho de um polígono
* a informação deve ser submetida e guardada na base de dados.


## dados reais
* usar os dados da Sérvia, coordenadas de celulas existentes. Atenção, que várias células podem estar "co-localizadas" no mesmo site (sitio), pois teem antenas a apontar para direções diferentes, ou usam frequencias diferentes

