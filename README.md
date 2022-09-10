## PyTech 
um agregador de conteudo em Django.

O pytech é um agregador de conteudo, virtual
extrai matéria de notíciarios de sites como
tech armazena-os na base de dados SQLITE.

## Requerimentos
django == 4.0.2
feedparser == 6.0.10

## Configuração de desenvolvimento
Executar as migrações: 
  - python manager.py makemigrations && python manager.py migrate

Executar um trabalho Django:
  - python manager.py startjobs

navegue até: http://127.0.0.1:8000/



## Meta
Samuel K Africano – kandunboafricano@gmail.com


## Contribuindo
1. Faça o _fork_ do projeto (<https://github.com/SamuelAfricano/agregadorDeconteudo/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_
