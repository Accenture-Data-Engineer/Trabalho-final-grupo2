<p align="center"> 
<a href="https://imgbox.com/hdeygBol" target="_blank"><img src="https://images2.imgbox.com/95/76/hdeygBol_o.jpeg" alt="image host"/></a>
</p>
<h1 align="center"> ANTI FRAUDE TECH S.A. </h1>
<h4 align="center"> Academia de mulheres em Tech - data engineer (azure) <a href="https://www.linkedin.com/company/accenture/">Accenture</a> <a href="https://www.linkedin.com/school/gama-academy/">e Gama Academy </a>(Verão 2023) </h4>

<br>
</br>
<p align="center"> 
<a href="https://imgbox.com/mlNPr8ij" target="_blank"><img src="https://images2.imgbox.com/aa/35/mlNPr8ij_o.gif" alt="image host" height="142px"/></a>
</p>

<h4><a href="#contexto">Contexto e objetivo</a> | <a href="#arquivos">Descrição dos arquivos</a> | <a href="#principais_ferramentas">Principais ferramentas</a> | <a href="#execucao">Instrução de execução</a> | <a href="#ferramentas">Ferramentas</a> | <a href="#creditos">Créditos</a> |</h4>

<h2 id="contexto"> :brain: CONTEXTO E OBJETIVO</h2>

<p>As fraudes em conta corrente podem ocorrer por meio de phishing, onde o fraudador envia e-mails falsos, mensagens de texto, ou utilizar técnicas de engenharia social, como manipulação psicológica, para obter informações confidenciais, como senhas e dados bancários. Também podem ocorrer por meio de skimming, onde os dados do cartão de crédito ou débito são roubados por meio de um dispositivo eletrônico instalado em um caixa eletrônico ou em um terminal de pagamento. Outra forma de fraude em conta corrente é o roubo de identidade, em que o fraudador usa informações pessoais roubadas para abrir contas falsas ou realizar transações em nome da vítima.</p>

<p>Tendo em vista que é muito importante tomar medidas de segurança para proteger sua conta corrente, desenvolvemos para as empresas bancárias uma aplicação em Python para carga de arquivos em um banco de dados SQL e geração de relatórios estatísticos, visando a descoberta dessas fraudes. O filtro da conta fraudada, foi contruído com base naquelas movimentações abaixo de 2 minutos de espaçamento entre as transações.</strong></p>  

<p>Observação: <i>É importante ressaltar que as informações referentes a contas correntes são consideradas dados sensíveis e, portanto, devem ser protegidas de forma adequada. No entanto, no contexto da avaliação deste trabalho, optamos por disponibilizar dados fictícios para ilustrar nossos resultados e análises.</i></p>

<h2 id="arquivos"> :floppy_disk: DESCRIÇÃO DOS ARQUIVOS DO PROJETO</h2>

<p>Esse projeto inclui arquivos executáveis e de destino, além de você conseguir acesso ao nosso diretório fonte (repositório), como a seguir:</p>
<h4>Arquivos executáveis:</h4>
<ul>
  <li><a href="xx"><b>connection.py</b></a> - Usado para conectar e popular nossos dados para o banco de dados da Azure via SQL Alchemy</li>
   <li><a href="xx"><b>main.ipynb</b></a> - Usado para criar esquemas das tabelas, limpeza e organização dados originais para se tornarem tratados</li>
   <li><a href="xx"><b>query_filtrar_fraudes.ipynb</b></a> - Usado para filtrar as fraudes (in, out e total) em Python com com PySpark e Pandas</li>
   <li><a href="xx"><b>migration.py</b></a> - Usado para realizar a conexão com o banco de dados e importar as tabelas para o Power BI com o Pandas</li>
   <li><a href="xx"><b>create_table.sql</b></a> - Usado para criar tabelas de cliente, transações e fraudes</li>
   <li><a href="xx"><b>fraud_view.sql</b></a> - Usado para criar visualização das fraudes utilizando SQL</li>
   <li><a href="xx"><b>state_code.sql</b></a> - Usado para criar tabela de estados para a tentaiva de gráfico por região em nosso Dashboard</li>
   <li><a href="xx"><b>projeto_final.pbix</b></a> - Usado para o arquivo final do Dashboard do Power BI com todas as measures finais</li>
</ul>

<h4>Arquivos de destino:</h4> 
<ul>
  <li><a href="https://github.com/Accenture-Data-Engineer/Trabalho-final-grupo2/blob/main/requirements.txt"><b>requirements.txt</b></a> - Contém as versões dos módulos/bibliotecas utilizadas nos nossos códigos</li>
  <li><a href="https://github.com/Accenture-Data-Engineer/Trabalho-final-grupo2/blob/main/docker-compose.yaml"><b>docker-compose.yaml</b></a> - Contém o código de configurações para utilização do PySpark e Jupyter notebook</li>
  <li><a href="https://github.com/Accenture-Data-Engineer/Trabalho-final-grupo2/tree/main/data/clients"><b>pasta clients</b></a> - Contém os csv ligados aos clientes, os datasets originais e os nossos já tratados</li>
  <li><a href="https://github.com/Accenture-Data-Engineer/Trabalho-final-grupo2/tree/main/data/transaction"><b>pasta transaction</b></a> - Contém os csv ligados as transações, os datasets originais e os nossos já tratados</li>
  <li><a href="https://github.com/Accenture-Data-Engineer/Trabalho-final-grupo2/tree/main/data/fraudes"><b>pasta fraude</b></a> - Contém os csv ligados a fraudes, separados por fraudes totais, de transações Out (dinehiro que saiu) ou In (dinheiro que entrou)</li>
</ul>

<h4>Diretório fonte:</h4>
<ul>
  <li><a href="https://github.com/Accenture-Data-Engineer/Trabalho-final-grupo2"><b> Trabalho-final-grupo2</b></a> - Inclui todos os arquivos listados acima </li>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="principais_ferramentas"> :book: PRINCIPAIS FERRAMENTAS UTILIZADAS </h2>

<p>Primeiramente, utilizamos o<strong>Spark</strong> que é uma biblioteca de processamento de dados distribuído que oferece uma plataforma escalável para análise e processamento de grandes volumes de dados em tempo real. Sua importância reside na sua capacidade de acelerar o processamento de dados através da execução em paralelo em clusters de servidores, permitindo a execução de algoritmos sofisticados em grandes conjuntos de dados.

No contexto de detecção de fraudes, o Spark é especialmente útil para analisar conjuntos de dados para detectar padrões e anomalias que possam indicar atividades fraudulentas. O PySpark tornou-se uma ferramenta essencial dentro do nosso trabalho para a detecção de fraudes, permitindo a identificação e ação imediata em transações suspeitas feitas em contas de clientes com um intervalo menor que 2 minutos, ajudando a prevenir perdas financeiras e proteger a segurança dos usuários de conta corrente.</p>

<p>Também contamos com o auxílio da bibliteca <strong>Pandas</strong> nos Dataframes, já que tal ferramenta, além de posuir compatibilidade com o Spark, auxilia com sua melhor visualização do Dataframe, com facilidade de uso, por ser mais popular e ter filtragens de dados melhor documentadas. O Pandas também foi utilizado para a conexão com o SQL Server para população e atividades do nosso banco de dados.</p>

<p>Utilizamos, ainda, a <strong>Azure</strong> que é uma plataforma de computação em nuvem oferecida pela Microsoft, que fornece uma ampla variedade de serviços de infraestrutura e aplicativos para empresas. A Azure foi importante para o uso de máquinas virtuais e bancos de dados nas fraudes de conta corrente, pois permitiu ao nosso grupo criar e gerenciar esses recursos de forma rápida, conjunta e escalável, além de fornecer alta disponibilidade, segurança e desempenho.</p>

<p>Além disso, trabalhamos com o <strong>SQL</strong>, que é uma linguagem de programação utilizada para gerenciar e manipular bancos de dados relacionais. Ela permitiu a criação, atualização e consulta dos nossos dados no banco de dados, através do <strong>SQL Server</strong> que é um sistema de gerenciamento de banco de dados relacional da Microsoft que utiliza a linguagem SQL. Quando utilizamos em conjunto com a plataforma Azure, o SQL Server se tornou uma solução altamente escalável e flexível para armazenamento e processamento de dados, permitindo que nosso grupo gerenciasse nossos bancos de dados de forma eficiente e sem conjunto na nuvem.</p>

<p> Por fim, utilizamos o <strong>Power BI</strong>, uma ferramenta de business intelligence desenvolvida pela Microsoft, que permite a criação de dashboards e relatórios interativos com base em dados de diversas fontes. Para o nosso dashboard de fraudes de conta corrente, o Power BI foi importante por permitir a visualização clara e rápida dos dados, bem como a criação de gráficos e tabelas que facilitam a identificação de padrões e anomalias. Com o uso do Power BI, foi possível reunir informações de diversas fontes, como transações bancárias e dados de clientes, e consolidá-las em um único painel, tornando a análise mais eficiente e precisa.</p>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="execucao"> :clipboard: INSTRUÇÃO DE EXECUÇÃO</h2>
<p>A ordem de possível execução dos arquivos do programa a seguir, deve ser executada após realizar o dowload do arquivo ZIP do <a href="https://github.com/Accenture-Data-Engineer/Trabalho-final-grupo2"><b>nosso caderno</b></a>:</p>

<p><b>1) Contextualização e entendimento da organização</b></p>
<p>Antes de iniciar qualquer trabalho é essencial entender o contexto do que se trata, por isso indicamos que você leia todas as notas feitas neste documento e se sentir necessário esquise mais sobre o assunto. Para ajudar você a entender como pensamos e montamos este projeto, indicamos que você entre no nosso <a href="https://github.com/orgs/Accenture-Data-Engineer/projects/2">Miro</a> que foi nossa fonte de Brainstorm do tema e o que queriamos do projeto final, das tabelas, fluxograma, measures e muito mais, e junto indicamos ver o nosso <a href="https://github.com/orgs/Accenture-Data-Engineer/projects/2">Kanban</a> onde temos toda a organização e tarefas que realizamos drante o projeto para chegar no nosso Dashboard final.
  
<p><b>2) Arquivos CSV (as tabelas que utilzamos para todo o projeto)</b></p>
<p>Caso você queira checar nossos dados e realizar sua próprias análises, deve separar os principais datasets tratdos, dentre eles dentro da pasta "data" temos uma outra pasta "clients", na qual você pode acessar a pasta "clients_clean" e usufruir de qualquer um dos csv ali dispostos. Utilizando o mesmo caminho você pode acessar as transações abrindo a pasta de "transaction" e depois "transaction_clean". Por fim abra a pasta "fraudes" e acesse ou o dataset principal "dataset_fraude.csv", ou o dataset com as fraudes de entrada "dataset_fraudes_in.csv", ou apenas o dataset com fraudes de saída "dataset_fraudes_out.csv".</p>

<p><b>3) Arquivos executáveis (arquivos que podem ser modificados e analisados para entender os processos)</b></p>
<p>Você pode explorar qualquer um dos nossos arquivos executáveis, descritos aqui no tópico "Descrição dos arquivos do projeto". Os arquivos com extensão .py ou .ipynb são ligados a códigos de Python utiliados para fazer a limpeza e organização dos dados, a filtragem de fraudes ou para a conexão dos dados com a Azure ou Power BI. Também possuímos os arquivos com extensão .sql, que sâo utilizados para as measures do nosso Dashboard, diferente do nosso arquivo com extensão .pbix que você pode visualizar o arquivo final do Power BI do nosso Dashboard.</p>

<p><b>4) Dashboard Power BI</b></p>
<p>Caso você não queira abrir os arquivos, disponibilizamos aqui o link para nosso dashboard interativo. Nele, você pode obter diversos insights, questionamentos e filtragens por categorias ou dados únicos.</p>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="ferramentas"> :books: FERRAMENTAS </h2>
<ul>
  <li>Azure</li>
   <li>Power BI</li>
    <li>Python</li>
   <li>PySpark</li>
   <li>Pandas</li>
    <li>SQL Server</li>
    <li>Docker compose</li>
    <li>DAX</li>
    <li>SQL Alchemy</li>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="creditos"> :scroll: CRÉDITOS</h2>

<table>
  <tr>
    <td width="300px">
      <p align="center">
      <img src="https://images2.imgbox.com/30/33/VK9BKcTB_o.png" alt="image host" height="142px"/>
        </p>
      <h3 align="middle">Anna Lígia Nogueira</h3>   
      <p align="center">
      <a href="https://github.com/ligianogueira1"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"  height="25px"></a>
      <a href="https://www.linkedin.com/in/anna-ligia-alves-nogueira/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="25px"></a>
        </p>
    </td>
    <td width="300px">
      <p align="center">
      <img src="https://images2.imgbox.com/be/82/h2zVhrnK_o.png" alt="image host" height="142px"/>
        </p>
      <h3 align="middle">Amanda Carvalho de Oliveira</h3>
      <p align="center">
      <a href="https://github.com/jonesamandajones"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height="25px"></a>
      <a href="https://www.linkedin.com/in/amanda-oliveira-jones/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="25px"></a>
        </p>
    </td>
    <td width="300px">
      <p align="center">
      <img src="https://images2.imgbox.com/85/5b/XE03SXix_o.png" alt="image host" height="142px"/>
        </p>
      <h3 align="middle">Bruna Bellini Faria</h3>
      <p align="center">
      <a href="https://github.com/brunabellini"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height="25px"></a>
      <a href="https://www.linkedin.com/in/brunabellinifaria/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="25px"></a>
        </p>
  </tr>

<table>
  <tr>
     </td>
    <td width="300px">
      <p align="center">
      <img src="https://images2.imgbox.com/0a/7c/qSbcQK5o_o.png" alt="image host" height="142px"/>
        </p>
      <h3 align="middle">Cintia Fasioli</h3>
      <p align="center">
      <a href="https://github.com/CintiaFasioli"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height="25px"</a>
      <a href="http://linkedin.com/in/cintiafasioli"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="25px"></a>
        </p>
    </td>
    <td width="300px">
      <p align="center">
      <img src="https://images2.imgbox.com/1e/d2/RF6Lg3Zw_o.png" alt="image host" height="142px"/>
        </p>
     <h3 align="middle">Lais Oliveira Melo</h3>                  
      <p align="center">
      <a href="https://github.com/Lasmelo"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height="25px"></a>
      <a href="https://www.linkedin.com/in/laisoliveiramelo/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="25px"></a>
        </p>
    </td>
   <td width="300px">
      <p align="center">
      <img src="https://images2.imgbox.com/cf/6f/2Q7TlyTi_o.png" alt="image host" height="142px"/>
        </p>
      <h3 align="middle">Nathália Martins</h3>
      <p align="center">
      <a href="https://github.com/martinsnathalia"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height="25px"></a>
      <a href="https://www.linkedin.com/in/nathaliamartinss/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="25px"></a>
        </p>
    </td>
   </tr>
  
 <table>
  <tr>
    <td width="300px">
      <p align="center">
      <img src="https://images2.imgbox.com/53/3a/E28kOnFO_o.png" alt="image host" height="142px"/>
        </p>
      <h3 align="middle">Sabrina Alves</h3>
      <p align="center">
      <a href="https://github.com/Sabrina-alv"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height="25px"></a>
      <a href="https://www.linkedin.com/in/sabrina-alves-1aa201209"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"  height="25px"></a>
        </p>
      <td width="600px">
        <p align="center"> Orientadores e Yellow Belt</p>
        <p align="center">
        <img src="https://images2.imgbox.com/fa/c2/sB1RO5nd_o.jpeg" alt="image host" height="120px"/>
         <img src="https://images2.imgbox.com/40/85/oAMwTMOI_o.jpeg" alt="image host" height="120px"/>
         <img src="https://images2.imgbox.com/6e/3b/s9CBuXB9_o.jpeg" alt="image host" height="120px"/>
         </p>
        <h3 align="middle">Camila Avila&emsp;Danilo Aparecido&emsp;Ynna</h3>
       </td>
  </tr>
