class ImoveisCaixa():
    def __init__(self, link, endereco, bairro, descricao, preco, avaliacao, desconto, modalidade_venda, foto, cidade, estado):
        self.link_imovel = link
        self.endereco = endereco
        self.bairro = bairro
        self.descricao = descricao
        self.preco = preco
        self.avaliacao = avaliacao
        self.desconto = desconto
        self.modalidade_venda = modalidade_venda
        self.foto = foto
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return self.descricao
    
    def exibir_imovel(self):
        pass


#teste de classe
# imovel_caixa = ImoveisCaixa ('<link>', 'rua', 'bixiga', 'centroVelho', 15000, 250000,'20%','leilão','#','Guarulhos','SP')


import requests
from bs4 import NavigableString
from bs4 import Tag
from bs4 import BeautifulSoup

class ExtrairImoveis():

    def acessa_ximoveis(self, url):
        response = requests.get(url)

        if response.status_code == requests.codes.ok:
            
            soup = BeautifulSoup (response.text, 'html.parser')
            tabela = soup.find('table')

            lista_imoveis = []

            for imovel in tabela.find('tr'):

                if isinstance(imovel, NavigableString):
                    continue
                if isinstance(imovel, Tag):
                    # print(body_child.name)
                    # link             = imovel.find('a', href=True)
                    link             = imovel.find_all('td')[0].text.strip()
                    endereco         = imovel.find_all('td')[1].text.strip()
                    bairro           = imovel.find_all('td')[2].text.strip()
                    descricao        = imovel.find_all('td')[3].text.strip()
                    preco            = imovel.find_all('td')[4].text.strip()
                    avaliacao        = imovel.find_all('td')[5].text.strip() 
                    desconto         = imovel.find_all('td')[6].text.strip()
                    modalidade_venda = imovel.find_all('td')[7].text.strip()
                    foto             = imovel.find_all('td')[8].text.strip()
                    cidade           = imovel.find_all('td')[9].text.strip()
                    estado           = imovel.find_all('td')[10].text.strip()
                    print(link)

                # cria objeto    
                # imovel_caixa = ImoveisCaixa (link, endereco, bairro, descricao, preco, avaliacao, desconto, modalidade_venda, foto, cidade, estado)
                
                # cria lista de objetos
                # lista_imoveis.append(imovel_caixa)

        else:
            raise TypeError ("site fora do ar, código http:", response.status_code)
            
       
url = 'https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.htm?'
rotina = ExtrairImoveis()
tabela = rotina.acessa_ximoveis(url)

            


