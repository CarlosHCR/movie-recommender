<h1>Projeto Django Rest Framework para Sugestão de Filmes</h1>

<h2>O projeto utiliza uma API de inteligência artificial para recomendação de filmes baseada em preferências de gênero e tipo de filme fornecidas pelos usuários.</h2>

<p>Este projeto utiliza Django Rest Framework e PostgreSQL em Docker para criar uma API que gera sugestões de filmes utilizando inteligência artificial e os armazena no banco de dados.</p>

<h2>Pré-requisitos</h2>

<p>Antes de começar, você precisa ter os seguintes softwares instalados no seu computador:</p>
<ul>
  <li><a href="https://git-scm.com">Git</a></li>
  <li><a href="https://www.docker.com/">Docker</a></li>
  <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
  <li><a href="https://www.python.org/downloads/">Python 3.12+</a></li>
</ul>

<h2>Tecnologias</h2>

<p>Este projeto foi desenvolvido com as seguintes tecnologias:</p>

<ul>
  <li><a href="https://workspace.google.com/intl/pt-BR/solutions/ai/?utm_source=google&utm_medium=cpc&utm_campaign=latam-BR-all-es-dr-BKWS-all-all-trial-e-dr-1707806-LUAC0020236&utm_content=text-ad-none-any-DEV_c-CRE_694677572535-ADGP_Hybrid+%7C+BKWS+-+EXA+%7C+Txt-Gemini-Meet-KWID_43700079796748902-kwd-2235429706214&utm_term=KW_generative%20ai%20google%20meet-ST_generative+ai+google+meet&gad_source=1&gclid=CjwKCAjwtNi0BhA1EiwAWZaANNGaK5eRHFRocsHmmVkXv5EWm1rLvLFvYJ8osYdK3VXxxJB6DLkyzBoCKo4QAvD_BwE&gclsrc=aw.ds">Google Generative AI</a></li>
  <li><a href="https://www.django-rest-framework.org/">Django rest framework</a></li>
  <li><a href="https://swagger.io/">Swagger</a></li>
</ul>

<h2>Clonando o Projeto</h2>

<p>Para baixar o projeto, clone este repositório no seu terminal com o seguinte comando:</p>

<pre>
  <li><a href=""><code>git clone https://github.com/CarlosHCR/movie-recommender.git</code></a></li>
</pre>

<h2>Certifique-se de estar na pasta do projeto</h2>

<h4>Configurar variáveis de ambiente</h4>

<pre>
  <li><a href=""><code>Renomeie o arquivo .env.example para .env e configure as variáveis de ambiente necessárias, incluindo chaves de API para a API de inteligência artificial.</code></a></li>
</pre>

<h4>Iniciando Docker</h4>

<pre><li><a href=""><code>docker-compose up -d --build</code></a></li></pre>

<h4>Rodando o Backend (Django)</h4>

<p>Crie um ambiente virtual e ative-o:</p>

<pre>
  <li><a href=""><code>python -m venv venv</code></a></li>
  <li><a href=""><code>Win: venv\Scripts\activate</code></a></li>
  <li><a href=""><code>Linux/MacOs: source venv/bin/activate</code></a></li>
</pre>

<p>Atualize o PIP</p>

<pre>
  <li><a href=""><code>pip install --upgrade pip</code></a></li>
</pre>

<p>Instale as dependências</p>

<pre>
  <li><a href=""><code>pip install -r requirements.txt</code></a></li>
</pre>

<p>Faça as migrações do banco de dados</p>

<pre>
  <li><a href=""><code>python manage.py makemigrations</code></a></li>
  <li><a href=""><code>python manage.py migrate</code></a></li>
</pre>

<p>Inicie o servidor</p>

<pre>
  <li><a href=""><code>python manage.py runserver</code></a></li>
</pre>

<p>O servidor estará rodando em <code>http://localhost:8000</code>.</p>

<p>Acessando a API via Swagger <code>http://localhost:8000/swagger/</code> </p>
