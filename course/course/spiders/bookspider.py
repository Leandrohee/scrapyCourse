import scrapy


class BookspiderSpider(scrapy.Spider):                          # Criado automaticamento na hora de criar a spider
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):                                 # Nome da funcao criada automaticamente na hora de criar a spider
        books = response.css('article.product_pod')            # Pegando a referencia HTML e CSS dos livros do site "article" representa a tag html e ".product_pod" representa a classe dessa tag

        for book in books:                                                      # Pegando todos os livros achados na pagaina
            yield {                                                             # Yield é para criar um gerador ao invez de uma lista que ocupe espaço
                'name': book.css('h3 a::text').get(),                           # a::text pega o texto detro da tag html
                'price': book.css('.product_price .price_color::text').get(),
                'url': book.css('h3 a').attrib['href'],                         # maneira 1 de escrever o codigo
                'url': book.css('h3 a:attr(href)').get()                        # maneira 2 de escrever o codigo acima
            }

        nextPage =  response.css('li.next a ::attr(href)').get()                    # Pega a caminho Url relativo no botao Next Page na pagina

        if nextPage is not None:
            if 'catalogue' in nextPage:
                nextPageUrl = 'https://books.toscrape.com/' + nextPage
            else:
                nextPageUrl = 'https://books.toscrape.com/catalogue/' + nextPage
            yield response.follow(nextPageUrl, callback=self.parse)                 # Chama a funcao parse novamente com a proxima pagina como parametro