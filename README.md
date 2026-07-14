# Alura Album - Copa do Mundo Tech 🚀

Este projeto é um **Álbum de Figurinhas Virtual e Interativo** com a temática "Copa do Mundo Tech". Ele foi desenvolvido como parte da **Imersão Alura (Julho de 2026)** e celebra grandes mentes da computação e da tecnologia, divididas em categorias temáticas, incluindo pioneiros internacionais e celebridades do ecossistema tech do Brasil.

O álbum conta com um design visual premium (estilo futurista/dark mode) e simula a experiência física de folhear um álbum real, com direito a efeito visual de dobra de páginas em 3D e efeito sonoro de papel sintetizado dinamicamente.

---

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é demonstrar a construção de uma aplicação web interativa rica em recursos visuais e auditivos, explorando:
1. **Manipulação avançada do DOM** e integração de bibliotecas JavaScript terceiras para efeitos tridimensionais de páginas de livro/álbum.
2. **Síntese de áudio em tempo real** usando a **Web Audio API** para gerar efeitos sonoros de fricção e virada de papel dinamicamente (sem depender de arquivos estáticos de áudio).
3. **Consumo de APIs assíncronas** integrando um front-end estático com um back-end FastAPI para carregar imagens e informações das figurinhas de forma dinâmica.

---

## 📁 Estrutura do Projeto e Funcionalidades dos Arquivos

O projeto está estruturado nos seguintes diretórios e arquivos principais:

### 1. Diretório `figurinhas-main/`
Contém as imagens das figurinhas das personalidades da tecnologia organizadas numericamente de `#01` a `#30`.
* **Conteúdo**: Arquivos de imagem em formatos como `.jpg`, `.png`, `.webp`, `.avif` e `.jpeg`.
* **Personalidades inclusas**:
  * Pioneiros de IA (Alan Turing, John McCarthy, Geoffrey Hinton, Yann LeCun, etc.)
  * Criadores do ecossistema Python (Guido van Rossum, Tim Peters, Raymond Hettinger, etc.)
  * Gigantes dos Bancos de Dados (Edgar F. Codd, Larry Ellison, Salvatore Sanfilippo, etc.)
  * Criadores de Sistemas Operacionais e Linguagens de Base (Linus Torvalds, Dennis Ritchie, Steve Jobs, Bill Gates, etc.)
  * Nomes de destaque da comunidade de tecnologia do Brasil (Paulo Silveira, Guilherme Silveira, Gustavo Guanabara, Maurício Aniche, Rafaela Ballerini, Guilherme Lima, Giovanna Souza, Vinicius Neves, etc.)

---

### 2. Diretório `i-arq-ia-alura-album-main/`
Contém o código-fonte da aplicação front-end. Os arquivos envolvidos e suas respectivas funções são descritos abaixo:

#### 📄 [index.html](file:///c:/Users/caike/Documents/imersão arquitetura web da alura/i-arq-ia-alura-album-main/index.html)
Define a estrutura semântica HTML5 do álbum.
* **Capa e Contracapa**: Estrutura a identidade visual da capa com elementos decorativos holográficos, logotipo dinâmico com efeito glitch e colagem de mini cards. A contracapa contém a sinopse do projeto e um código de barras simulado.
* **Organização das Páginas**:
  * **Página 1 (Pioneiros da Inteligência Artificial)**: Espaço para as figurinhas `#01` a `#05`.
  * **Página 2 (Arquitetos da Simplicidade - Python)**: Espaço para as figurinhas `#06` a `#10`.
  * **Página 3 (Arquitetos de Bancos de Dados)**: Espaço para as figurinhas `#11` a `#15`.
  * **Página 4 (Arquitetos da Computação Moderna - OS)**: Espaço para as figurinhas `#16` a `#20`.
  * **Páginas 5 e 6 (Celebridades Tech - Brasil - Vol. 1 e 2)**: Espaço para as figurinhas `#21` a `#30`.
* **Dependências Externas**: Carrega a biblioteca interativa `PageFlip` via CDN (`page-flip.browser.min.js`) e fontes personalizadas do Google Fonts (`Inter` e `Outfit`).

#### 📄 [style.css](file:///c:/Users/caike/Documents/imersão arquitetura web da alura/i-arq-ia-alura-album-main/style.css)
Contém a folha de estilos responsável pelo visual futurista e pela responsividade da aplicação.
* **Design de Cores & Efeitos**: Utiliza variáveis CSS para definir uma paleta de cores harmoniosa baseada em tons de azul profundo, ciano neon e preto espacial. Implementa o efeito Glitch e brilhos holográficos (glow) na capa.
* **Diagramação e Layout**: Define grades complexas (`CSS Grid`) para os slots das figurinhas e organiza o viewport tridimensional no qual o livro é renderizado.
* **Efeitos de Transição e Dobra**: Adiciona sombras de dobra na lombada do livro (`::after` nas páginas pares/ímpares) e estilos específicos para as figurinhas inseridas dinamicamente via JS (animação de transição suave de "colagem" de figurinha).
* **Estados Interativos**: Modifica cursores do mouse (`grab` / `grabbing`) para indicar a possibilidade de arrastar as páginas.

#### 📄 [app.js](file:///c:/Users/caike/Documents/imersão arquitetura web da alura/i-arq-ia-alura-album-main/app.js)
Contém toda a lógica comportamental e dinâmica da aplicação. Suas principais responsabilidades são:
1. **Inicialização do `St.PageFlip`**: Configura a biblioteca de virada de página física com limites de tamanho, sombras e restrições de eventos padrão, implementando em seguida um controle personalizado de arraste (`mousedown`, `mousemove`, `mouseup` e eventos de toque para celular) para proporcionar uma experiência fluida.
2. **Navegação Inteligente**: Escuta eventos de clique nas setas laterais de navegação e eventos de teclado (teclas de seta esquerda/direita). Oculta/exibe botões dinamicamente com base na página atual (ex: esconde seta esquerda na capa).
3. **Síntese de Efeito Sonoro**: Utiliza a **Web Audio API** para gerar um som realista de papel virando em tempo real. Cria e mixa ruído branco (White Noise) com filtros passa-banda e passa-baixa, controlados por um envelope de volume dinâmico.
4. **Mapeamento e Preenchimento de Figurinhas**: Realiza uma requisição assíncrona (`fetch`) para a API backend (`http://localhost:8000/figurinhas`), analisa o retorno em JSON contendo o mapeamento das imagens e insere dinamicamente as tags `<img>` nos respectivos slots `#01` a `#30` com animação de fade-in.

---

## 🛠️ Tecnologias Utilizadas

* **HTML5** & **CSS3** (Flexbox, Grid, Variáveis, Animações)
* **JavaScript (ES6)**
* **Web Audio API** (Osciladores, Filtros e Envelopes de Áudio)
* **Biblioteca PageFlip** (Efeito 3D de livro interativo)
* **FastAPI / Python** (Provedor do serviço backend de dados das figurinhas)

---

## 🚀 Como Executar o Projeto

1. **Servindo o Front-end**:
   * Abra a pasta `i-arq-ia-alura-album-main` e execute um servidor web estático local (como a extensão *Live Server* do VS Code ou via terminal com `npx serve .` ou `python -m http.server 8080`).
   * Acesse a URL gerada no seu navegador (ex: `http://localhost:5500` ou `http://localhost:8080`).

2. **Iniciando o Backend (API)**:
   * Para carregar as fotos das figurinhas dinamicamente no álbum, inicialize a API backend conforme as instruções da imersão (exemplo: navegue até o diretório do backend e execute):
     ```bash
     cd backend/dia-3
     uvicorn main:app --reload
     ```
   * Por padrão, a aplicação espera que a API esteja rodando no endereço `http://localhost:8000`.

---

Desenvolvido com carinho durante a Imersão Alura 💻✨
