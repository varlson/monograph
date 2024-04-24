# RESUMO

O presente repositório refere-se a um projeto em Python utilizado no desenvolvimento da minha monografia no curso de Ciência da Computação na Universidade Federal de Ouro Preto. O projeto tem o título **"A correspondência entre a estrutura da rede de mobilidade e os casos de COVID-19 no Brasil"**.

# SOBRE MONOGRAFIA

Com o propósito de investigar a relação entre a mobilidade das pessoas e os casos de COVID-19 no Brasil, este estudo busca aplicar abordagens de redes complexas para modelar e ilustrar a importância das redes de mobilidade na propagação de epidemias, como a COVID-19. Uma compreensão profunda desse fenômeno é crucial para a tomada de decisões no enfrentamento de epidemias similares. Foram utilizados dados de mobilidade aérea (referentes a 2019), fluvial e terrestre (ambos de 2016) do Instituto Brasileiro de Geografia e Estatística (IBGE), juntamente com dados de casos de COVID-19 (de fevereiro de 2020 a maio de 2021) do Ministério da Saúde do Brasil.
Redes foram construídas a partir dos dados de mobilidade, tendo as cidades como nós e as conexões entre cidades como arestas, representando os fluxos de deslocamento entre elas. Métricas de centralidade da rede, como grau, _betweenness_ e _closeness_ serão computadas a partir da rede para se investigar as correspondências entre elas e os dados de notificação de casos de COVID-19.
Espera-se que os resultados deste estudo forneçam ferramentas eficazes para embasar decisões relacionadas à mobilidade de pessoas no contexto do combate a epidemias semelhantes à COVID-19.

# ESTTRUTURA DO PROJETO

monograph/
├── LICENSE
├── networkSorter.py
├── plots/
├── folderStructure.py
├── networkBuilder.py
├── correspondeceCalculator.py
├── README.md
├── plotter.py
├── .gitignore
├── datas/
├── ├── aerial.csv
├── ├── graphs/
├── ├── ├── merged.GraphML
├── ├── ├── terrestrial.GraphML
├── ├── ├── aerial.GraphML
├── ├── ├── fluvial.GraphML
├── ├── cases-brazil-cities-time.csv
├── ├── aerial.GraphML
├── ├── cities_coord.csv
├── networkMerger.py
├── folterStructure.txt
├── requirements.txt
├── results/
├── ├── plots/
├── ├── ├── aerial/
├── ├── ├── ├── aerial.png
├── ├── ├── fluvial/
├── ├── ├── ├── fluvial.png
├── ├── sorted/
├── ├── ├── merged/
├── ├── ├── ├── strength/
├── ├── ├── ├── ├── strength.csv
├── ├── ├── ├── closeness_w/
├── ├── ├── ├── ├── closeness_w.csv
├── ├── ├── ├── betweenness_w/
├── ├── ├── ├── ├── betweenness_w.csv
├── ├── ├── ├── closeness/
├── ├── ├── ├── ├── closeness.csv
├── ├── ├── ├── betweenness/
├── ├── ├── ├── ├── betweenness.csv
├── ├── ├── ├── degree/
├── ├── ├── ├── ├── degree.csv
├── ├── ├── aerial/
├── ├── ├── ├── strength/
├── ├── ├── ├── ├── strength.csv
├── ├── ├── ├── closeness_w/
├── ├── ├── ├── ├── closeness_w.csv
├── ├── ├── ├── betweenness_w/
├── ├── ├── ├── ├── betweenness_w.csv
├── ├── ├── ├── closeness/
├── ├── ├── ├── ├── closeness.csv
├── ├── ├── ├── betweenness/
├── ├── ├── ├── ├── betweenness.csv
├── ├── ├── ├── degree/
├── ├── ├── ├── ├── degree.csv
├── ├── ├── terrestrial/
├── ├── ├── ├── strength/
├── ├── ├── ├── ├── strength.csv
├── ├── ├── ├── closeness_w/
├── ├── ├── ├── ├── closeness_w.csv
├── ├── ├── ├── betweenness_w/
├── ├── ├── ├── ├── betweenness_w.csv
├── ├── ├── ├── closeness/
├── ├── ├── ├── ├── closeness.csv
├── ├── ├── ├── betweenness/
├── ├── ├── ├── ├── betweenness.csv
├── ├── ├── ├── degree/
├── ├── ├── ├── ├── degree.csv
├── ├── ├── fluvial/
├── ├── ├── ├── strength/
├── ├── ├── ├── ├── strength.csv
├── ├── ├── ├── closeness_w/
├── ├── ├── ├── ├── closeness_w.csv
├── ├── ├── ├── betweenness_w/
├── ├── ├── ├── ├── betweenness_w.csv
├── ├── ├── ├── closeness/
├── ├── ├── ├── ├── closeness.csv
├── ├── ├── ├── betweenness/
├── ├── ├── ├── ├── betweenness.csv
├── ├── ├── ├── degree/
├── ├── ├── ├── ├── degree.csv
├── ├── intersections/
├── ├── ├── aerial/
├── ├── ├── ├── aerial.csv
├── ├── ├── terrestrial/
├── ├── ├── ├── terrestrial.csv
├── ├── ├── fluvial/
├── ├── ├── ├── fluvial.csv
├── ├── filtred/
├── ├── ├── aerial_filtred_covid_cases_data.csv
├── ├── ├── terrestrial_filtred_covid_cases_data.csv
├── ├── ├── fluvial_filtred_covid_cases_data.csv
├── main.py # **Arquivo principal**
├── util.py

# DEPENDENCIAS

    - matplotlib==3.8.4
    - networkx==3.3
    - numpy==1.26.4
    - pandas==2.2.2
    - pycairo==1.20.1
    - scipy==1.13.0
    - igraph==0.11.4

    Tambem será necessário a execução de seguinte comando para a instação dos demais libs:
    sudo apt-get install texlive-latex-extra texlive-fonts-recommended dvipng cm-super

O ficherio "cases-brazil-cities-time.csv" pode ser encontrado no seguinte link: [https://github.com/wcota/covid19br/blob/master/DESCRIPTION.md](https://github.com/wcota/covid19br/blob/master/DESCRIPTION.md)
