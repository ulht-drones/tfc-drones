# tfc-drones

## 1. representação de objetos (fazer 25.4.2022)

1. Criar os seguintes classes/objetos no models:
   * centro do mapa
   * drone (incluir como campos tambem a) frequencia, b) potencia transmitida, c) diagrama de radiação - charfield (anexo um exemplo de ficheiro de texto).
   * célula (incluir como campos tambem a) frequencia, b) potencia transmitida, c) diagrama de radiação - ficheiro json)
   * polígono da área de serviço
   * heatmap da zona iluminada pelo drone. usa para já a imagem em baixo. representa-a sobre o mapa com a propriedade "opacity: 0.5", por forma a que tenha transparencia que permita visualizar o mapa


heatmap:
![heatmap](https://user-images.githubusercontent.com/42048382/165084159-6e416fad-fd9c-4491-8660-98c6e869e3ef.png)


2. Criar objetos no admin de cada tipo. 
* centrar mapa na universidade da Sérvia. 
* representar celulas e drone nessa zona.
* inventar polígono em volta do estadio de futebol
* sobrepor imagem sdo heatmap por cima do poligono

3. na função view ir buscar esses objetos e envia-los no context para o HTML

4. Inserir no mapa no HTML os objetos

5. incluir no relatório esta informação, sobretudo visualização dos 4 tipos de objetos

## 2.  desenho de polígono (fazer 26.4.2022)

* implementar a funcionalidade de desenho de um polígono
* a informação deve ser submetida e guardada na base de dados.


## 2. dados reais
* usar os dados da Sérvia, coordenadas de celulas existentes. Atenção, que várias células podem estar "co-localizadas" no mesmo site (sitio), pois teem antenas a apontar para direções diferentes, ou usam frequencias diferentes

