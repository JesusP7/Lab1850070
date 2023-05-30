## Webscraping

Esta sección contiene 2 scipts de Python:

- **Scrape_quote.py**

	Utilizando las librerías: requests, csv y BeautifulSoup, la tarea de este scipt es la de realizar Webscraping a una página en específico (http://quotes.toscrape.com/), Primero realiza una petición a la URL del sitio, después analiza el contenido HTML del sitio y finaliza haciendo una lista con las citas y los autores, la cual muestra y guarda en un archivo .csv.
	
- **Scrap12.py**

	Utilizando las librerías: requests y BeautifulSoup, la tarea de este scipt es la de realizar Webscraping a una página en específico (https://realpython.github.io/fake-jobs/), Primero realiza una petición a la URL del sitio, después BeautifulSoup formateara información recibida por la página y una vez realizado esto el script buscara metadatos para obtener información, en específico este script busca información sobre trabajos relacionados a Python, es capaz de encontrar, el titulo del post, la compañia que lo pública, la localización y el link asociado al post.
