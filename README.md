# Cloud Computing

Resumo/Transcrição dos slides de aula da disciplina Computação em Nuvem

> **Observação**: caso tenha `[...]` em algum tópico, isso implica que eu não terminei a anotação, sendo necessário olhar os slides diretamente.

# Introdução

## Introdução à Computação em Nuvem

### História

[...]

#### Evolução

[...]

#### Primeiros passos 

[...]

#### Amazon EC2 (Elastic Compute Cloud) - 2006

[...]

#### Amazon S3 (Simple Storage Service)

[...]

#### Amazon RDS (Relational Database Service)

[...]

#### Google Apps e a Computação Empresarial

[...]

#### Google App Engine - 2008

[...]

### Computação em Nuvem na visão moderna

[...]

#### Definição

##### NIST

"Modelo para habilitar **acesso conveniente e sob demanda a um pool compartilhado de recursos** configuráveis de computação que podem ser **rapidamente provisionados e liberados** com **esforço mínimo de gerenciamento ou interação com o provedor de serviços**"

##### Gartner

"Estilo de computação no qual **capacidades de TI escaláveis e elásticas são fornecidas como um serviço** para clientes externos usando **tecnologias da internet**"

##### Forrester

"Capacidade de TI padronizada entregue via tecnologias da internet de maneira **paga por uso e de autoatendimento**"

#### Resumo

- **Menos impostos**: gastos em cloud entram como despesas e não como investimentos
- **Sob demanda**
- **Mais escalabilidade**
- **Menos osciosidade**: paga somente pelo uso, se tiver usando pouco, reduz a máquina e paga menos
- **Infraestrutura ágil**: menor investimento inicial e instalação rápida através de autoatendimento

#### Caraterísticas

- **Elasticidade**: capacidade de **aumentar ou diminuir recursos automaticamente conforme demanda**
  - atua de forma **reativa** e **automática**, corrigindo picos e quedas.
  - depende de paramêtros pré configurados como limite de uso, mínimos e máximos, etc
  - não requer planejamento prévio, age depender dos limites.
- **Escalabilidade**: capacidade de **adicionar ou remover recursos conforme a necessidade**, sem interrupções para suportar mais carga. Normalmente planejado, como cenários da black friday e outros.
  - ajuste conforme a demanda
  - capacidade de escalar ou reduzir rapidamente para atender a picos de uso sem superdimensionamento ou subutilização
- **Flexibilidade**: capacidade da infraestrutura de se adaptar a diferentes necessidades, estando relacionado a liberdade de escolha e adapção estrutural, como por exemplo a alterar infraestrutura física do hardware, ligar/desligar remotamente, etc.
  - trocar uma VM com GPU por outra; mudar engine de DB;
  - diferentes ambientes
  - alterar configurações de rede ou segurança
- **Pagamento por uso**: modelo de cobrança baseado no **consumo real de recursos**
- **Redução de custo e agilidade**: menos investimento em compra e manutenção de infraestrutura física e custos operacionais previsíveis.
- **Agilidade Organizacional**: rapidez na implementação de soluções com tempo de provisionamento de recursos significativamente mais rápidos, permitindo adaptação às mudanças do mercado e flexibilidade estrutural mais rápido.

#### Desafios e Riscso

##### Segurança e Privacidade

A proteção de dados sensíveis torna um dos pontos críticos na migração para cloud, necessitando garantir a confidencialidade, integridade e disponibilidade dos dados, uma vez que perde o controle físico do acesso. 
Para tal, é necessário implementar medidas de seguranças robustas como criptografia e controle de acesso.
Mover dados de negócios para a nuvem compartilha a responsabilidade de segurança com o provedor, aumentando a exposição de dados e criando desafios adicionais de segurança.

##### Dependência do Fornecedor

Existe o risco de **lock-in** e falta de flexibilidade. 
Cada fornecedor possui suas especifidades que tornam-se diferenciais competitivos. No entanto, essas especificidades tornam-se impeditivos na migração de fornecedores devido a sua exclusividade. Neste caso mostra-se a importância de escolher fornecedores que ofereçam interoperabilidade e padrões abertos.

##### Complexidade no gerenciamento

A migração pra cloud traz complexidade no gerenciamento, sendo necessário novas habilidades, ferramentas e mão de obra especializadas no provedor, tal qual o a implantação de ferramentas de automação e monitoramento para garantir eficiência operacional.
Um ponto crítico geral no uso de cloud é que investigação forense não permite acesso a logs de máquina, dificultando perícias.

Além disso, ao utilizar cloud, parte da infraestrutura passa a ser operada pelo provedor. A organização mantém a responsabilidade pela governança do ambiente, mas menor controle direto sobre a infraestrutura física e processos operacionais.

##### Conformidade Legal

A localização física dos dados pode ser desconhecida, criando desafios de conformidade com regulamentos locais governamentais.

#### Raízes Tecnológicas

##### Clustering

**Grupo de recursos de TI independentes interconectados atuando como um único sistema**. Aumenta a disponibilidadade e confiaiblidade dos serviços devido à redundância e aos mecanismos de falha embutidos.

Algumas das características incluem:
- **Homogeneidade**: componentes tem hardware e SOs semelhantes;
- **Alta disponibilidade**: redundância e failover embutidos aumentam a confiabilidade;
- **Localização**: normalmente no mesmo datacenter;
- **Comunicação**: comunicação rápida e eficiente através de links dedicados.

Pode ser:
- **Horizontal**: adição de mais máquinas ou nós ou cluster
  - **Escalabilidade**: adicionar mais nós;
  - **Disponibilidade**: + capacidade de processamento e resiliência
  - **Uso comum**: aplicações que necessitam de load balancer como servidores web
  - Quando usar: cenários onde a carga de trabalho pode ser distribuída em múltiplos nós
- **Verticial**: aumento da capacidade dos nós existentes (upgrade de recursos como CPU e RAM)
  - **Performance**: aumenta a performance de cada nó individualmente
  - **Complexidade**: mais caso e complexo devido a limitações de hardware
  - **Uso comum**: aplicações que exigem alta performance em um único nó, como database.
  - Quando usar: aumento da capacidade em um único nó é mais eficiente que adicionar novos nós, tal qual onde a latência e a velocidade de acesso são críticas.

Resumo das diferenças:
- **Escalabilidade**: horizontal adiciona nós, verticial os melhora;
- **Custo**: horizontal pode ser mais econômico e flexível, vertical pode ser mais caro e complexo;
- **Aplicações**: horizontal para LB e resiliência, vertical para alta preformance em nós únicos.

##### Grid Computing

**organiza recursos computacionais em pools lógicos**, formando um **supercomputador virtual**. Difernete do clustering, o grid é mais distribuído e heterogêneo, permitindo recursos dispersos e variados trabalhem juntos de forma paralela.

Algumas das características incluem:
- **Heterogeneidade**: pode incluir recursos com diferentes hardwares e SOs;
- **Distribuição geográfica**: recursos podem estar dispersos;
- **Escalabilidade**: capacidade de incluir recursos adicionais facilmente;
- **Flexilbidade**: utiliza middleware para coordenar recursos, permitindo maior felxibilidade na alocação e uso

##### Diferenças entre Grid e Clustering

- Clusters são homogeneros e grids são heterogeneos;
- Clusters são localizados, grids são distribuídos;
- clusters usam links dedicados, grids usam middleware para coordenação;
- Clusters são usados para alta disponibilidade/LB, grids são usados para alta performance distribuída.

##### Virtualização

É a tecnologia que **permite a criação de instâncias virtuais de recursos físicos de TI**, permitindo que **múltiplos usuários compartilhem as capacidades de processamento subjacentes sem estarem vinculados ao hardware físico**. Gestão e alocação de recursos de maneira **flexível e eficiente**.

##### Conceitos e terminologia básica

###### Cloud ou nuvem

**Ambiente de TI projetado para o provisionamento remote de recursos escaláveis e medidos**. A nuvem permite que serviços sejam **escalados conforme a necessidade**, atendendo as demandas variáveis de forma eficiente.

###### Recursos de TI

Podem ser físicos ou virtuais, abrangendo servidores físicos e softwares personalizados. Essenciais para a operação de serviços em nuvem.

###### On-premise

Recursos on-premise são hospedados dentro de um limite organizacional tradicional e não são baseados em nuvem.
Oferecem maior controle e segurança locais, mas exigem maiores investimentos iniciais e custos operacionais contínuos.

###### Consumidores e provedores

Consumidores são entidades que utilizam recursos de TI baseados em nuvem.
Provedores são entidades que fornecem recursos e gerenciam a infraestrutura subjacente, garantindo que os serviços sejam entregues de maneira eficiente e segura.

##### Tipos de escalabilidade

##### Escalabilidade Horizontal

**Envolve a adição ou remoção de recursos do mesmo tipo**, conhecida como scaling out e scaling in.

##### Escalabilidade Vertical

**Refere-se à substituição de recursos por outros de capacidade diferente**, conhecida como scaling up e scaling down.

##### Diferenças entre os tipos de escalabilidade

<table>
  <thead>
    <tr>
      <th>Escalabilidade Horizontal</th>
      <th>Escalabilidade Vertical</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mais barata (hardware genérico - commodity)</td>
      <td>Mais caro (hardware específico)</td>
    </tr>
    <tr>
      <td>Recursos de TI disponíveis de imediato</td>
      <td>Recursos de TI disponíveis de imediato</td>
    </tr>
    <tr>
      <td>Replicação de recursos automatizada</td>
      <td>Configuração adicional específica necessária</td>
    </tr>
    <tr>
      <td>Necessidade de mais recursos de TI</td>
      <td>Não é necessário mais recursos de TI</td>
    </tr>
    <tr>
      <td>Não é limitado pela capacidade intrínseca do hardware</td>
      <td>Limitado à capacidade máxima do hardware</td>
    </tr>
  </tbody>
</table>

##### Benefícios do Cloud Computing

- Redução de investimento inicial
- Custos proporcionais sob demanda
- Flexibilidade e escalabilidade

# Funções e Tipos de Serviços

## Fundamentação e Modelos de Serviço

### Funções e Limites

- Governança e terceirização: como os recusos de TI são gerenciados e utilizados
- Compreender responsabilidades e controle sobre os recursos em um ambiente de cloud, limites organizacionais, confiança e segurança.

#### Roles

##### Provedor

Aquele que  **provê/disponibiliza o serviço**, incluindo armazenamento, processamento e serviços de rede. Além de fornecer, também gerencia a infraestrutura para garantir que os serviços sejam entregues de acordo com os SLAs

##### Consumidor

Aquele que  **utiliza os serviços fornecidos pelo provedor**. O acesso aos recursos é feito através de interfaces programáticas como APIs e aplicativos web.
Ele tem como responsabilidade gerenciar a utilização dos recursos de nuvem de forma eficaz para obter os benefícios da migração.
Aquele que **compra serviços de cloud e revendem para ampliar suas ofertas de serviços se enquadram como consumidor e provedor**.

##### Proprietário

Aquele que  **possui legalmente um serviço na nuvem, implicando responsabilidades legais e de manutenção**. Pode ser tanto o provedor quanto o consumidor, depende de quem desenvolveu e implantou o serviço.
Por exemplo quem desenvolve um software e disponibiliza-o na nuvem pode ser tanto consumidor (usa a infra de um provider), quanto um proprietário (detém os direitos do software).

##### Administrador de recursos de nuvem

Aquele que **gerencia os recursos de TI na nuvem, tanto a nível interno (atuando no consumidor) e externo (atuando no provedor)**. Tem como papel manter a disponibilidade, segurança e desempenho dos serviços oferecidos.

##### Auditor

Aquele que **realiza avaliações independentes da segurança, privacidade e desempenho dos serviços na nuvem a fim de construir confiança**.

##### Broker

Aquele que **atua como intermediario, negociando e gerenciando a utilização de serviços entre consumidores e provedores**. Um exemplo é o pacote Office da PUC, o qual não é comprado diretamente na Microsoft, mas sim através de um intermediario.

##### Carrier

Aquele que **fornece a conectividade de rede necessária para que consumidorees possam acessar os serviços em nuvem**

#### Limites Organizacionais - _Organizational Boundary_

Representa a fronteira física que circunda os recursos de TI de uma organização, delimitando quais recursos estão sobre sua propriedade e controle direto. Por exemplo contratar serviços de cloud e não querer que um funcionario específico do provedor controle seus serviços. Apesar de ser possível, o provedor pode negar, uma vez que não tem acesso direto ao limite organizacional do provedor.

#### Limite de confiança - _Trust Boundary_

Fronteira lógica que se estende para incluir componentes do ambiente de nuvem nos quais a organização decide confiar, como serviços ou infraestruturas de terceiros.

#### Exercicio

[...]

#### Características

- **Elasticidade** que permite a **escalabilidade** automática;
- **Uso sob demanda**;
- **Resiliência**, que assegura a continuidade dos serviços mesmo diante de falhas.

##### Uso sob demanda

Permite que consumidores **provisionem e utilizem recursos de TI conforme a necessidade sem precisar de interação direta com o provedor**. Isso garante **flexibilidade e eficiência operacional**.

##### Acesso Ubíquo

Capacidade de **acessar recursos em qualquer lugar**.
Apesar da disponibilidade completa dos serviços, deve-se lembrar sobre os limites de rede, que inicialmente são completamente liberados mas devem ser bloqueados para garantir segurança.

##### Multitenancy (muitos locatários)

Capacidade de **disponibilização de recursos de TI para múltiplos consumidores de forma isolada** Cada consumidor (**tenant**) utiliza o serviço sem ter acesso aos dados ou configuranções dos outros, garantindo segurança e privacidade.
A aplicação deve manter segregação de performance e recursos**, uma vez que se o usuário do Tenant A utilizar 100% dos recursos, não deve afetar a utilização do usuário do Tenant B.

##### Pooling de Recursos

É o conceito de que os provedores podem agrupar recursos de TI como armazenamento e processamento, para atender a vários consumidores simultaneamente, otimizando o uso dos recursos disponíveis. Este modelo é eficiente e permite uma melhor alocação de recursos de acordo com as necessidades variáveis dos consumidores. Muitas vezes utilizado em ambientes **multitenant** para dar flexibilidade na alocação dinâmica de recursos e melhorar a disponibilidade.

##### Elasticidade

Refere-se à capacidade de um sistema em núvem **ajustar automatizamente os recursos de TI**, escalando-os para cima ou para baixo conforme necessidade dentro dos limites pré-configurados.
Para o funcionamento da elasticidade vertical transparente, é necessário que o Hypervisor do SO da máquina seja ser orientado a eventos e suportar adição e remoção de recursos dinâmicamente sem reboot. Além disso, o Guest OS deve ter suporte a Hot-add-on, para entender quando ocorre alocação de CPU ou RAM e adaptar o sistema. No entanto, ele não entende de forma natural a desalocação (Hot-Remove). Para solucionar, é necessário subir uma nova instância, transferir os usuários conectados para a nova e realizar o desligamento da instância alterada.

##### Pay as you go

Capacidade da plataforma de nuvem de monitorar e registrar o uso dos recursos permitindo a cobrança precisa conforme o uso real. Além de servir como base para a cobrança, fornece dados para monitoramento e otimização de serviços a fim de ajustar suas ofertas para todos os consumidores.

##### Resiliência

Capacidade de um sistema de se recuperar rapidamente de falhas e continuar operando sem interrupções significativas. Pode ser obtida através da replicação de recursos e dados em múltiplas localizações físicas (datacenters diferentes), garantindo que se um componente falhas, outro possa assumir automaticamente a carga de trabalho.

##### Estudo de caso

[...]

### Ofertas e Serviços

#### IaaS - Infrastructure as a Service

Aluguel de infraestrutura de TI virtualizada (aluguem de VMs, redes, armazenamento). Esses recursos são provisionados e gerenciados pelo provedor, mas cabe ao consumidor a responsabilidade pela gerencia do SO, como upgrades, manutenção, etc.
Ideal para organizações que necessitam de alto nível de controle sobre a infraestrutura de TI, garantindo personalização e escalabilidade dos recursos. Alta flexibilidade, mas alta complexidade na gestão.
Se compra o serviddor virtual com 32GB RAM, 4GB de local storage, 99.5% de disponibilidade sem falhas por $0.95 a hora e $0.05 por GB tranfesrido na rede.

#### PaaS - Platform as a Service

Ambiente completo e pré-configurado onde os desenvolvedores sobem o código e já funciona. Neste cenário o provedor administra a infraestrutura, sendo responsavel por manter o SO, permitindo que os desenvolvedores concentrem-se apenas no desenvolvimento.
Se compra uma aplicação de alta disponibilidade por $0.45 a hora ou 500.000 requests com 99.5% de disponibilidade com auto-scaling.

#### SaaS - Software as a Service

Sofware é hospedado e mantido pelo provedor e disponibilizado aos consumidores via internet. Os consumidores não precisam se preocupar com a instalação, manutenção ou instalação do software ou infraestrutura, limitando sua gestão ao uso e às configurações disponibilizadas pela aplicação.
Se compra acesso a aplicação cobrando $0.05 a cada 100 requests com um response time de 0.5ms

# Tipos de Núvem

## Tipos de Nuvem

### Conceito de Nuvem Pública

- Ambiente de núvem acessível ao público, de propriedade e mantido por um provedor tercerizado, de forma que múltiplos usuários compartilhem recursos via internet.
- Aluguel de recursos computacionais.
- Vantagens:
  - Escalabilidade;
  - Custo reduzido;
  - Ausência de manutenção por parte do usuário.
- Menor controle sobre aspectos de segurança e personalização dos serviços.
- Exige atenção a custos, configurações e segurança.
- Provedor ganha dinheiro no **oversubscription**, ou seja, vende muito recurso e nunca é utilizado 100% da cota.
- Usos: aplicativos web que exigem flexibilidade e alta disponibilidade; ambientes de desenvolvimento e testes;

### Conceito de Nuvem Privada

- Infraestrutura cloud exclusiva para uma única organização, podendo ser interna ou mantida por um provedor (mas sempre com uso dedicado à organização proprietária).
- Maior controle sobre os recursos e dados, personalização e segurança.
- Custos mais elevados e requer um gerenciamento contínuo.
- Organização atua como provedor e consumidor dos recursos de TI.
- Usos: setores regulados que exisgem alta segurança dos dados ou personalização.

### Núvem privada é mais que um datacenter

**Possuir servidores/datacenter próprio não é necessariamente nuvem privada**, pois ela **precisa implementar caracteristicas específicas de cloud**, como por exemplo **automação, provisionamento sob demanda, elasticidade e gerenciamento centralizado sobre os recursos**.

### Conceito de Nuvem Comunitária

- Nuvem privativa dentro de um grupo de empresas para resolver o problema da nuvem privada ser cara, garantindo a customização. Similar a uma nuvem pública, mas restrito a uma comunidade específica de usuários que comparitlham interesses ou requisitos comuns.
- Permitem o compartilhamento de custos e recursos entre os membros, além de garantir conformidade com normas específicas do setor.
- Frequentemente usada em setores regulatórios como saúde e finanças para cumprir regulações específicas; projetos colaborativos entre diferentes organizações com objetivos e necessidades similares.
- O problema: governança da nuvem. Quem irá administrar e ser responsável pelas decisões? Quais decisões podem ser tomadas?
  - Custos e recursos compartilhados, políticas de segurança comuns.
  - A solução: joint-venture, uma nova empresa onde todos são societários para gerencia da cloud.

### Conceito de Nuvem Híbrida

- Oferece flexibilidade para as organizações permitindo a combinação de elementos de núvem pública, privada e/ou comunitária. 
- Usos: expansão de recursos, migrações graduais, resiliência e continudade de serviços, segurança dos dados (armazenamento dos dados em núvem privada e disponibilidade em nuvem pública)
- O problema: fazer os ambientes trabalharem juntos, necessitando de conectividade segura, maior complexidade de gerenciamento e sincronização, controle de acessos etc.

```mermaid
flowchart LR
    A("BD | App | Web\nAzure")
    B("BD | App | Web\nPrivada")
    C("Proxy Reverso")
    D("Internet")

    A --> C
    B --> C
    C --> D
```

### Comparando os tipos de nuvem

- A nuvem pública oferece menor controle, mas é mais econômica e escalável, sendo mantida por terceiros.
- A nuvem privada proporciona alto controle e segurança, mas a um custo maior, sendo exclusiva para uma única organização.
- A nuvem comunitária compartilha recursos e custos entre membros de uma comunidade específica, combinando segurança e conformidade com regulamentações.
- A nuvem híbrida integra aspectos dos outros modelos, oferecendo flexibilidade, mas com desafios adicionais na gestão e integração dos ambientes.

### Nuvem Híbrida e Multicloud

Apesar de serem conceitos relacionados, **não são a mesma coisa**. Multicloud reduz a dependência de um único fornecedor, mas ainda utiliza apenas nuvens públicas. Já a nuvem híbrida alterna entre diferentes tipos de ambientes.

### Edge Computing

Para reduzir latência, implementa mini datacenters ao lado de antenas 5G para processamento de dados em tempo real.

### Serverless

Provedor gerencia grande parte da infra necessária para executar uma aplicação, deixando o desenvolvedor focado no código. Recursos sob demanda através de triggers, como schedulers, endpoints de API entre outros.

### Nuvem Soberana e Soberania dos Dados

Alguns cenários é necessário controlar não apenas quem acessa os dados, mas também onde estão armazenados e suas legislações locais. A depender da legislação, o governo pode ter acesso a dados sensíveis.

### RBAC - Role Based Access Control

Protocolo de controle de permissão por grupos

```mermaid
%%{init: {
  "flowchart": {
    "nodeSpacing": 15,
    "rankSpacing": 20
  },
  "themeVariables": {
    "fontSize": "14px"
  }
}}%%

flowchart LR

    subgraph azure["Azure"]
        direction LR

        subgraph tenant1["Tenant"]
            direction TB

            subgraph sub1["Subscription"]
                direction LR
                rg1["Resource Group"]
                rg2["Resource Group"]
            end
        end

        subgraph tenant2["Tenant"]
            direction TB

            subgraph sub2["Subscription"]
                direction LR
                rg3["Resource Group"]
                rg4["Resource Group"]
            end
        end
    end

    style azure fill:none,stroke:#000,stroke-width:2px
    style tenant1 fill:none,stroke:#000,stroke-width:1.5px
    style tenant2 fill:none,stroke:#000,stroke-width:1.5px
    style sub1 fill:none,stroke:#000,stroke-width:1px
    style sub2 fill:none,stroke:#000,stroke-width:1px
```

Onde:
- Tenant: empresa
- Subscription: site/projeto
- Resource Group: subdivisões internas

### Explorando a Azure

#### Ambiente Privado dentro de uma Nuvem Pública

O Azure organiza seus recursos em camadas administrativas que ajudam a controlar custos, permissões, políticas e sepração entre ambientes.
[...]

# Responsabilidade Compartilhada

## Tipos de serviços e Responsabilidade Compartilhada

### Tipos de Serviço

#### IaaS: Infrastructure as a Service

É a **categoria mais flexível de cloud**, permite **locação de infraestrutura** como um serviço. Nela o provedor é responsável por manter o hardware, conectividade de rede e segurança física, enquanto o consumidor é responsável por todo o resto, desde configurar e manter o SO, até lidar com a aplicação.

##### Cenários

###### Migração _Lift-and-shift_

Processo de transformação inicial na migração para nuvem, configurando recursos de forma semelhante ao original.
Um processo encontrado nesta etapa é o P2V (Physical to Virtual), que gera uma imagem de sistema bootavel para virtualizar no formato Hypervisor, convertendo o SO com drivers de CPU físico (ex. Intel Core XX) para uma CPU genérica.

##### Teste e desenvolvimento

O consumidor define configurações de ambiente para replicação rápida.

#### PaaS: Platform as a Service

**Locação de plataforma para deployment**. Em um ambiente PaaS, o **provedor mantém as responsabilidades** que mantinha em um **IaaS**, mas adicionalmente também é **responsável por manter o SO, middlewares, ferramentas de desenvolvimento** etc. Enquanto isso, o **cliente não precisa se preocupar com licença ou atualizações de SOs**, **focando no processo de desenvolvimento de software** sem comprometer a infraestrutura de execução.

##### Cenários

[...]

##### PaaS com Orquestração de Containers: Docker Swarm e Kubernetes

- **Escalabilidade automatizada com múltiplos Pods**: garante resiliência e balanceamento de carga automatico conforme a demanda.
- **Orquestração com Kubernetes**: autoescalonamento, rollouts automáticos, gerenciamento de estado desejados. Garantindo alta disponibilidade e manutenção contínua sem downtime.
- **Swarm como alternativa simples**: orquestração básica de serviços integrada ao Docker com menos complexidade operacional.
- **Automação de deploys e monitoramenteo**: integração de pipelines CI/CD e ferramentas de monitoramento, reduzindo esforço manual na manutenção e confiabilidade da operação.
- **Responsabilidade compartilhada na orquestração**: provedor gerencia a infra e a plataforma de orquestração, enquanto o cliente lida com as configurações do serviço, políticas de escalabilidade e segurança dos containers.

#### SaaS: Software as a Service

Modelo de serviço mais completo a nível de produto, **alugando um aplicativo desenvolvido, instalado e configurado**, como por exemplo e-mail, CRM etc. **Menos flexível mas mais fácil de iniciar o uso**, necessitando de menos conhecimento técnico.

##### Cenários

[...]

### Responsabilidade Compartilhada nos Diferentes Modelos de Serviço em Cloud

Cada modelo de serviço possui uma divisão específicas de responsabilidades

#### IaaS

##### Responsabilidades do Provedor

- **Infraestrutura física**: gerenciamento e manutenção dos servidores, redes e storage;
- **Segurança física**: controle de acesso físico;
- **Disponibilidade**: garantia de uptime da infra e provisionamento de recursos.

##### Responsabilidades do Cliente

- **SO**: instalação, configuração e manutenção;
- **Segurança de rede**: configuração e gerenciamento de firewalls e grupos de segurança;
- **Dados e aplicativos**

##### Detalhes adicionais

###### Monitoramento e Logging

- **Provedor**: ferramentas básicas para monitoramento da infra;
- **Cliente**: monitorar o desempenho e segurança do sistema.

###### Patching e Atualizações

- **Provedor**: patches na infra física e hypervisor;
- **Cliente**: patches no SO da VM e em softwares instalados.

###### Escalaiblidade e Elasticidade

- **Provedor**: capacidades de escalabilidade automática;
- **Cliente**: configurar políticas de escalabilidade.
  
#### PaaS

##### Responsabilidades do Provedor

- **Infraestrutura e plataforma**: gerenciamento da infraestrutura subjacente e ferramentas de dev;
- **Segurança do ambiente**: aplicação de patches e atualizações de segurança;
- **Disponibilidade da plataforma**: garantia de uptime e manutenção dos serviços.

##### Responsabilidades do Cliente

- **Desenvolvimento de aplicativos**;
- **Gerenciamento de dados**: proteção e conformidade dos dados usados;
- **Configuração de acesso**: controle de acesso e permissões, tanto na aplicação quanto no acesso a cloud (tal qual AWS IAM).

##### Detalhes adicionais

###### Integração e API Management

- **Provedor**: fornecer APIs e serviços integrados;
- **Cliente**: integrar serviços de terceiros e gerenciar dependências de API.

###### Segurança de Aplicativos

- **Provedor**: garantir segurança no ambiente de execução e ferramentas;
- **Cliente**: garantir segurança dentro dos apps (RBAC).

###### Escalabilidade

- **Provedor**: fornecer mecanismos de escalabilidade automática
- **Cliente**: configurar políticas de escalabilidade

#### SaaS

##### Responsabilidades do Provedor

- **Aplicativo e infraestrutura**: gerenciamento total do software e infra;
- **Segurança e conformidade**: garantir segurança, proteção de dados e conformidade com regulamentos;
- **Disponibilidade e desempenho**.

##### Responsabilidades do Cliente

- **Gerenciamento de acessos**;
- **Proteção de dados**: garantia de integridade e segurança dos dados inseridos;
- **Conformidade de uso**.

##### Detalhes adicionais

###### Configuração e Personalização

- **Provedor**: fornecer opções de personalização dentro dos limites da aplicação;
- **Cliente**: configurar para atender às necessidades de negócio.

###### Backup e Recuperação de Dados

- **Provedor**: backups regulares e recuperação em caso de falha;
- **Cliente**: poder solicitar backups adicionais e gerir dados de acordo com políticas de retenção.

###### Atualizações Automáticas

- **Provedor**: atuaolizações automáticas;
- **Cliente**: ajustar fluxos de trabalho em resposta às atualizações.

#### Comparação entre modelos

- **IaaS**: maior **controle** e **responsabilidade do cliente**
- **PaaS**: responsabilidades **equilibradas**, com **foco** do cliente **no desenvolvimento** e segurança dos apps.
- **SaaS**: responsabilidade **mínima** para o cliente, focado principalmente na gestão de acesso e uso seguro dos dados.

![Responsabilidade entre modelos](assets/responsabilidade.png)

#### Considerações sobre segurança

Para garantir a eficácia na segurança, é necessário colaboração entre cliente e provedor, implementando práticas robustas em cada camada.
Alguns dos riscos comuns incluem:
- **IaaS**: falha na configuração do SO e rede;
- **PaaS**: vulnerabilidade em apps;
- **SaaS**: gestão inadequada de acessos.

#### Desafios

- **Complexidade e escalabilidade** em especial em ambientes híbridos dificultam com muitos níveis de controle e responsabilidade;
- **Conformidade** para evitar violações de conformidade e penalidades regulatórias;
- **Monitoramento contínuo** para garantir que todas as responsabilidades estão sendo cumpridas.

#### Boas práticas

- **Contratos claros** definindo resopnsabilidades de cada parte;
- **Educação contínua** através de treinamentos;
- **Ferramentas de segurança e monitoramento** para garantir segurança e desempenho contínuo.

# Cloud Maturity Model

## Cloud Maturity Model

O CMM foi originalmente desenvolvido para apoiar organizações no planejamento e evolução da adoção de cloud. 
Seu propósito é auxiliar as organizações a avaliar seu estado atual de maturidade em nuvem e definir o estado desejado de acordo com seus objetivos de negócio, identificando lacunas entre a situação atual e a desejada, criando um roadmap de evolução.
Permite avaliar a adoção considerando aspectos organizacionais e tecnológicos relacionados a governança, processos, pessoas e tecnologia.

### Níveis de Maturidade no CMM

- **Nível 0 - Legacy**: sistemas legados sem adoção de nuvem;
- **Nível 1 - Initial, Ad-hoc**: uso inicial e não coordenado de nuvem;
- **Nível 2 - Repeatable, Opportunistic**(Repetitivo): uso consistente com processos replicáveis, mas ainda exploratório;
- **Nível 3 - Defined, Managed**(Gerenciado): processos definidos e gerenciamento sistemático da núvem;
- **Nível 4 - Measured, Measurable**(Mensurado): uso avançado com métricas e otimização;
- **Nível 5 - Optimized**(Otimizado): Uso totalmente otimizado, alinhado com os objetivos de negócio

Não é necessário que todas as empresas adotem o nível 5 de maturidade. Cada caso é um caso, as vezes é exagero.

### Estrutura da Avaliação

O CMM não avalia somente infraestrutura ou tecnologias específicas, mas também diferentes domínios de maturidade que permitem analisar capacidades relevantes para adoção de cloud.
A versão atual contempla 31 domínios técnicos e não técnicos como finanças, cultura, compliance, comercial, arquitetura de TI, segurança, redes, etc. E cada um dos domínios podem possuir domínios diferentes.

### Níveis

#### Nível 0 - Legacy

Aplicações predominantemente executadas em infraestrutura tradicional _on-premise_ com poucos processos internos, sem uma estratégica ou abordagem definida para adoção de cloud

Desafios:
- Infraestrutura pouco flexível para mudanças;
- Processos de provisionamento manuais;
- Custos e capacidades frequentemente associados à aquisição antecipada de infraestrutura.

#### Nível 1 - Initial, Ad-hoc

Adoção inicial e não coordenada de serviços de nuvem. Processos podem existir, mas são manuais.
Uma prática comum é o ShadowIT, o uso de serviços de nuvem por áreas ou departamentos sem coordenação central do TI.
Uso básico de IaaS e SaaS como ferramentas de produtividade e colaboração. 

Desafios:
- Falta de controle centralizado e governança;
- Uso não planejado e sem políticas claras.

#### Nível 2 - Repeatable, Opportunistic

Uso sistemático da núvem com processos replicáveis, mas ainda exploratório, gerando inconsistência nos processos. Adoção em diferentes áreas da organização, mas sem um plano coeso (sem contrato formal por parte do TI).
Alguns dos padrões ja incluem ambientes de desenvolvimento e teste, além de modelo de pagamento _pay-as-you-go_.
Uso estruturado de IaaS para virtualização de servidores e armazenamento; uso inicial de PaaS para desenvolvimento de software e SaaS para colaboração e comunicação.

Desafios:
- Inconsistência na aplicação de práticas e políticas de nuvem;
- Foco em infraestrutura e serviços básicos.

#### Nível 3 - Defined, Systematic

Processos já definidos, gerenciamento sistemático de núvem com contratos personalizados e governança estabelecida.
Alguns dos padrões comuns incluem governança centralizada e práticas recomendadas de segurança como controle de acesso e monitoramente contínuo.
Uso de IaaS como automação básica e prática de DevOps, SaaS para integração com sistemas legados e funções críticas, PaaS para desenvolvimento. 

Desafios:
- Conformidade e segurança na escala de nuvem;
- Alinhamento entre TI e negócios

#### Nível 4 - Measured, Measurable

Uso mais avançado da núvem com métricas e otimização, com processos de medição e análise para monitorar desempenho.
Alguns dos padrões já incluem o uso de Infrastructure as Code (IaC) para gerenciar recursos através de texto, além de pipelines automatizadas de CI/CD (Continuous Integration/Continuous Deployment).
Como tecnologias inclue-se o uso de IaaS, PaaS, SaaS e FaaS (Function as a Service) para execução de funções sob demanda em ambientes serverless.

Desafios:
- Complexidade crescente;
- Otimização não comprometer segurança.

#### Nível 5 - Optimized

Uso totalmente otimizado e alinhado com os objetivos de negócio, buscando inovação contínua e uso de tecnologias emergentes.
Alguns dos padrões incluem tomada de decis˜ões baseadas em dados e desenvolvimento de aplicativos nativos para a nuvem.
Como tecnologia temos IaaS, PaaS, SaaS totalmente otimizados, FaaS, AI/ML e IoT

Desafios:
- Manter a inovação enquanto gerencia complexidade e risco;
- Sustentar vantagem competitiva através da inovação contínua.

### Implementação na prática

- **Definição do escopo**
- **Seleção dos domínios relevantes**
- **Avaliação do estado atual**
- **Definição do estado desejado**
- **Identificação dos gaps**
- **Roadmap**
- **Monitoramento**

### Benefícios

- **Avaliação estruturada**
- **Identificação de gaps**
- **Planejamento estratégico**
- **Alinhamento com o negócio**
- **Otimização de recursos**

### Desafios

- **Resistência a mudanças**
- **Complexidade na integração**
- **Governança e segurança**
- **Maturidade Desigual**
- **Subjetividade da avaliação**
- **Definição do nível-alvo**

# Bases Tecnológicas

## Redes para Datacenter

### Redes de Computadores

#### Redes Banda Larga e Arquitetura da Internet

- Redes banda larga **permitem a comunicação entre usuários e serviços**;
- A **internet como backbone**, conectando consumidores de nuvem a provedores de serviços;
- Além da internet pública, **conexões dedicadas** como MPLS (Multiprotocol Label Switching) e VPNs (Virtual Private Network) **para maior segurança e/ou desempenho**.

#### Arquitetura da Internet: Níveis

- **Tier 1**: grandes **provedores globais**, responsáveis pela interconexão de redes principais, como AT&T, Claro etc.
- **Tier 2**: **provedores regionais** que compram trânsito de redes Tier 1 e revendem para o nível 3.
- **Tier 3**: **ISPs** (Internet Service Providers) **locais** que compram transito nível 2 e revendem para usuários finais, como a Desktop, Laricel etc.

**A hierarquia de rede garante redundância e resiliência.**

#### Componentes da Arquitetura de Redes

- **Rede Orientada a Pacotes**: transmissão de dados de forma **independente** através da rede.
- **Roteadores e roteamento**: dispositivos que **determinam o caminho ideal para cada pacote baseado na topologia da rede e políticas de roteamento**. Um exemplo de protocolo é o BGP.
- **Protocolos de Rede**: protocolos como TCP/IP garantem a entrega ordenada e confável dos dados.
- **QoS (Qualidade de Serviço)**: técnicas para garantir a prioridade do tráfego em redes congestionadas em aplicativos sensíveis a latência como videoconferência.

#### Problemas de Conectividade na Nuvem

- **Latência**: tempo necessário para que um pacote viaje de um ponto a outro na rede. Crucial para performance em aplicações sensíveis ao tempo.
- **Largura de banda**: capacidade máxima de transmissão de dados entre dois pontos, influenciando diretamente a velocidade de acesso.
- **Jitter e Perda de Pacotes**: variações no atraso e pacotes que não chegam ao destino.
- **Soluções e Otimizações**: CDNs (Content Delivery Networks) para otimização de rotas e tecnologias de compressão de dados para melhorar a conectividade.

> Latência x Largura de Banda: latência é a velocidade no qual os pacotes trafegam na rede, enquanto a largura de banda é o quanto de pacote pode trafegar. 
> Pensando em uma analogia, largura de banda é a altura/espessura de um cano, quanto de agua pode passar, enquanto a latência é o comprimento/distância, indicando quanto tempo demora para sair do Ponto A até o Ponto B.

```mermaid
flowchart TB
    subgraph S[" "]
        direction LR
        A["A"] --- C["↕<br/>Largura de Banda"]
        C --- B["B"]
    end

    L["←─── Latência ───→"]

    S --- L

    style S fill:none,stroke:#333,stroke-width:2px
    style A fill:none,stroke:none
    style B fill:none,stroke:none
    style C fill:none,stroke:none
    style L fill:none,stroke:none
```

#### Seleção de Provedor e Operador de Nuvem

- **Impacto dos ISPs**: a qualidade da conexão depende das infraestruturas de ISP usados pelos consumidores e provedores;
- **Colaboração entre ISPs**: acordos de _peering_ e trânsito são essenciais para manter a qualidade e custo das conexões entre redes, em especial conexão entre diferentes países;
- **Custos e Complexidade de Implementação**: múltiplos provedores e caminhos redundantes para garantir alta disponibilidade e reduzir latência;
- **Critérios de Seleção**: SLA (Sevice Level Agreement - contratos), suporte técnico, compliance e segurança.

### Datacenters

**Instalação física que abriga servidores e demais componentes e recursos de TI essenciais**. Representam o **ponto central da infraestrutura de nuvem**, fornecendo recursos computacionais necessários para executar aplicativos e armazenar dados.
A centralização dos componentes em um datacenter é importante essencialmente por eficiência energética, manutenção, otimização de recursos e segurança física.
Os datacenters podem ser on-premise (corporativos/privativos), colocation (sublocação), gerenciados e cloud.

#### Estrutura do Datacenter

- **Camada Física**: hardware, infraestrutura de suporte a resfriação e energia;
- **Camada Virtualizada**: abstração de recursos físicos para a criação de ambientes virtualizados e isolados para um uso eficiente e flexível;
- **Plataformas de Gerenciamento**: sistemas de monitoramento e controle de recursos de TI para alocação, escalonamento e manutenção de serviços;
- **Redundância e Alta Disponibilidade**: estratégias para evitar falhas de serviço como fontes redundantes, backups automatizados etc.

#### Tecnologias Específicas para Gerenciamento de Datacenter

Datacenters modernos **exigem tecnologias especializadas para gestão eficiente de recursos**, garantindo eficiência operacional, redução de custos de manutenção, aumento na disponibilidade e segurança dos recursos de TI.

##### Switches KVM (Keyboard, Video, Mouse)

É um dispositivo que permite o controle de múltiplos servidores a partir de um único teclado, monitor e mouse.

Suas principais vantagens incluem:
- **redução do número de dispositivos de conectividade**, economizando espaço e energia;
- **gerenciamento remoto**, permitindo intervenções sem presença física;
- **rapidez na troca de servidores** durante manutenções periódicas, **facilitando a manutenção**;

##### Módulos RSA e HMC

Módulos RSA (Remote Supervisor Adapter) e HMC (Hardware Management Console) são cartões de gerenciamento remoto que oferecem controle completo sobre servidores, incuindo inicialização e monitoramento de hardware. 
Ambos possuem funcionalidades próximas mas aplicados em escalas diferentes. O HMC em especial é voltado para grandes sitemas legados como mainframes e permite gerenciar múltiplos servidores de uma vez, incluindo recursos de virtualização como LPARs.
Suas principais funções incluem gerenciamento e diagnóstico remoto, monitoramento de hardware como temperatura, ventoinhas e energia, logs e autenticação para segurança. Essas funcionalidades reduzem a necessidade de acesso físico ao datacenter, diminuindo o tempo de resposta a falhas e segurança da informação, além do monitoramento contínuo.

> LPAR: Abreviação de `Logical Partitions`, é basicamente uma quebra do hardware em partições lógicas usado em mainframe. Não é virtualização, é segregação de hardware.

#### Implementações Avançadas de Cabling

Cabeamento estruturado eficiente é essencial para desempenho e escalabilidade de datacenters.
Existem diferentes tipos de cabos, como os de cobre que são usados para conexões de curta distância e fibra óptica, utilizado em conexões de longa distância e alta velocidade dentro e entre datacenters.

Algumas das práticas incluem:
- Gerenciamento eficiente dos cabos com o uso de trilhos e braçadeiras para organização para evitar confusões e obstrução do fluxo de ar;
- Cabeamento redundante, implementando múltiplos caminhos para garantir resiliência;

> Uma forma comum de organização dos cabos é organizar a fiação por baixo do piso elevado e conecta-los diretamente aos hacks, que por sua vez são ordenados internamente através de switches e cabos pequenos.

#### Soluções de Resfriamentos de Datacenter

[...]

#### Gerenciamento de Energia

O consumo de energia elétrica é um dos maiores custos operacionais em datacenters. Neste cenário é essencial sistemas de gerenciamento de energia para monitoramento contínuo do consumo para identificar desperdícios e otimizar a disribuição para redução de custos e minimar o impacto ambiental.
Além disso, é necessário implementação de redundância para garantir disponibilidade ininterrupta através de múltiplas fontes de energia e sistemas de redundância.

##### UPS (Uninterruptible Power Supply)

Técnica para garantir disponibilidade ininterrupta através da redundância, fornecendo energia temporária durante quedas ou falhas de energia, protegendo equipamentos críticos.
Geradores a Diesel atuam como backup de longo prazo, fornecendo energia durante falhas prolongadas após esgotamento do UPS.

> Exemplo de datacenter que vi na internet: salas duplicadas de bateria, que permanecem ligadas somente durante a transição entre a energia elétrica e os geradores a diesel, garantindo disponibilidade.

> "Quem tem um não tem nenhum; Quem tem dois tem um". É essencial ter redundância, como por exemplo as "salas gemeas" para baterias, além de múltiplos provedores de diesel.

#### Segurança Física em Datacenters

- **Grades no teto** para evitar acessos não autorizados através de áreas adjacentes ou superiores. Uma barreira física adicional.
- **Autenticação Biométrico** como impresão digital ou reconhecimento facial para garantir que somente pessoas autenticadas possam acessar o datacenter.
- **Cartões de acesso** muitas vezes combinados com credenciais de segurança pessoal permitem o monitoramento de entrada e saída, além de permitir uma revogação rápida de permissões em cenários específicos.
- **Portas Eclusas** projetadas para garantir que somente uma pessoa entre por vez.
## Virtualização

### Introdução a Virtualização

Virtualização é o **processo de criar uma versão virtual de um recurso de TI**, como servidores, armazenamento e redes.
A virtualização permite uma **redução de custos em hardware físico**, **flexibilidade e escalabilidade na alocação e configuração de recursos**, além na **facilidade de gestão** a partir da centralização do gerenciamento de recursos.

### Componentes da Virtualização de Servidores

#### Hypervisor

Software que permite a criação e execução de VMS fornecendo uma **camada de abstração entre o hardware e os SOs virtuais**, **gerenciando a alocação de recursos para as VMs**, permitindo que **múltiplos SOs rodem em um único hardware físico**.

#### Maquinas Virtuais (VMs)

**Instâncias virtuais de SOs que operam em um ambiente isolado**, agindo como um servidor independente.

##### Imagens de VM

Arquivos que contém uma **cópia completa de um SO** para facilitar a **implantação rápida de novas VMs**, clonagem de ambiente e recuperação em crises.

##### Templates e Clones

Templates são **imagens de VMs pré-configuradas** usadas para criar novas VMs de forma consistente.
Clones são cópias exatas de VMs existentes. Clones podem ser parciais ou inteiros, reproduzem todas as configurações (inclusive MAC ADDRESS, que se não for alterado vai dar conflito no recebimento de pacotes caso duas instâncias estejam ativas).

### Componentes da virtualização de rede

#### Hypervisor de rede

Software que permite a **abstração dos recursos físicos de rede através de redes virtuais independentes**, facilitando a criação de múltiplas redes virtuais independentes dentro de uma única infraestrutura física.

#### Switches Virtuais (vSwitches)

Switches que **permitem e gerenciam o tráfego de rede virtual entre VMs** e permitem a segmentação de redes virtuais.

#### Roteadores Virtuais

Dispositivos virtuais que **desempenham funções de roteamento e encaminhamento de pacote entre sub-redes virtuais**.

#### Firewalls Virtuais

Software de firewall que protege redes ao **controlar o tráfego de entrada e saída da rede virtual** aplicando políticas de segurança similar a um dispositivo físico.

#### Controlador de Rede

Software que **gerencia e controla os recursos de rede virtual**, centralizando o gerenciamento e automação das operações de rede.

#### Overlay Networks (Redes de Sobreposição)

Redes virtuais **criadas sobre a infraestrutura de rede física** usando técnicas como VXLAN, GRE ou NVGRE, permitindo a extensão de redes virtuais através de diferentes locais físicos, facilitando a conectividade entre datacenters.

#### SDN - Software-Defined Network

Gerenciador de redes que permite criar e gerenciar redes através de software configurado via APIs

<!-- Mais detalhes [aqui](#)O que é SDN (Software Defined Network) -->

### RAID - Redundant Array of Independent Disk

É uma tecnologia que **combina múltipos discos usado para aumentar a performance ou redundância do armazenamento** dos dados.

#### RAID 0

Discos físicos atuam como um único disco virtual. Por exemplo, dois discos de 512GB atuam como um disco único de 1TB

```mermaid
flowchart LR
    subgraph RAID0["1 TB"]
        direction TB
        D1["512 GB"]
        D2["512 GB"]
    end

    style RAID0 stroke-width:3px
    style D1 stroke-width:2px
    style D2 stroke-width:2px
```

#### RAID 1

Discos físicos atuando como backup. 
Seu funcionamento depende da replicação de conteúdo entre discos de forma assíncrona (para evitar delay). Nesse cenário, dois discos de 512GB representam somente um único disco de 512GB.

```mermaid
flowchart LR
    subgraph RAID0["512 GB"]
        direction TB
        D1["512 GB"]
        D2["512 GB"]
    end

    style RAID0 stroke-width:3px
    style D1 stroke-width:2px
    style D2 stroke-width:2px
```

#### RAID 5

Funcionando com **no mínimo** 3 discos, realiza operações simultâneas e permite aumentar a redundância e armazenamento. 
Seu funcionamento é baseado em operações simultâneas em 2 discos e utiliza o 3 como uma forma de recuperação via paridade (XOR). A principal vantagem é que com 3 discos, somente 1/3 é backup.
```mermaid
flowchart LR
    subgraph RAID0["1 TB"]
        direction TB
        D1["512 GB"]
        D2["512 GB"]
        D3["512 GB"]
    end

    style RAID0 stroke-width:3px
    style D1 stroke-width:2px
    style D2 stroke-width:2px
    style D3 stroke-width:2px
```

<table>
    <thead>
        <tr>
            <td colspan="3" align="center">1 TB</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">1</td>
            <td align="center">0</td>
            <td align="center">[1]</td>
        </tr>
        <tr>
            <td align="center">[0]</td>
            <td align="center">0</td>
            <td align="center">0</td>
        </tr>
        <tr>
            <td align="center">1</td>
            <td align="center">[0]</td>
            <td align="center">1</td>
        </tr>
    </tbody>
</table>

No exemplo acima, se os bits (1, 0) são escritos respectivamente nos discos 0 e 1, através de 1 XOR 0 é possível saber que o valor de paridade é 1 (armazenado no 3 disco). Dessa forma, caso qualquer um dos 3 discos falhe, pode usar o terceiro como conta reversa para recuperar o dado perdido. No entanto, caso dois discos falhem, ai sim o dado é corrompido.

### Componentes de Virtualização de Storage

#### Hypervisor de Storage

Software que abstrai e gerencia os recursos físicos de armazenamento, facilitando a criação de volumes de armazenamento virtual que são independentes do hardware subjacente.

#### Storage Area Network (SAN) Virtual

Rede de armazenamento virtualizada para permitir o acesso a pools de storage compartilhados entre servidores.

#### Network Attached Storage (NAS) Virtual

Dispositivos NAS virtualizados para fornecer de forma centralizada o acesso a arquivos e dados através de uma rede padrão.

#### Pools de Storage

Conjuntos de recursos de armazenamento combinados em uma unidade lógica de armazenamento, permitindo o gerenciamento e a alocação dinâmica de armazenamento cmo base nas necessidades de aplicativos e cargas de trabalho.

#### Snapshots e Clones

Snapshots são cópias de estado de armazenamento em um ponto específico no tempo, enquanto clones são réplicas completas de volumes de armazenamento. Snapshots permitem a restauração rápida de dados, enquanto clones facilitam a replicação de backup de dados.

### Virtualização de Servidores

#### Tipos de Hypervisors

##### Hypervisor Bare-Metal 

Também conhecido como hypervisor tipo 1, é instalado diretamente sobre o hardware físico, proporcionando alto desempenho por possuir acesso direto aos recursos de hardware, além de oferecerem melhor segurança e isolamento para ambientes de virtualização que exigem alta confiança.
Temos como exemplo VMware ESXi, Microsoft Hyper-V, Xen e KVM (quando integrado ao kernel do Linux diretamente no hardware).

![Hypervisor Bare-Metal](assets/hypervisor-tipo1.png)

##### Hypervisor Hosted

Também conhecido como hypervisor tipo 2, é instalado sobre um sistema operacional já existente, facilitando o uso, mas reduzindo a eficiência. Devido o SO intermediário, adiciona uma camada adicional de software que pode introduzir sobrecarga no desempenho, além de depender de `syscalls` no SO host para acessar o hardware, limitando o desempenho.
São conhecidos pela facilidade no uso e configuração por serem instalados como um aplicativo padrão, mas reduzem o desempenho devido à sobrecarga do SO host.
Temos como exemplo VMWare Workstation, Oracle VirtualBox, Paralles Desktop, Microsoft Virtual PC.

![Hypervisor Hosted](assets/hypervisor-tipo2.png)

##### Diferenças entre Tipo 1 e Tipo 2

![Diferença entre os tipos de hypervisor](assets/diff-hypervisors.png)

> O ponto essencial aqui é que não necessariamente é preciso usar um hypervisor do tipo 1 se não for um servidor, vai aumentar muito a complexidade do acesso as máquinas pra casos simples

#### Gerenciamento de Recursos

- CPU e Memória: a alocação de recursos feita pelo hypervisor garante isolamento entre VMs, impedindo que uma VM acesse o recurso da outra;
- Armazenamento: discos virtuais são isolados;
- Rede: redes virtuais separadas logicamente usando VLANs e vSwitches para isolar o tráfego de rede de cada VM.

> Basicamente todos os recursos são isolados em cada VM.

##### Isolamento

- CPU e Memória: particionamento de CPU com técnicas como **CPU Pinning** e gerenciamento de memória pelo hypervisor;
- Armazenamento: discos virtuais isolados e técnicas de file locking;
- Rede: VLANs e vSwitches garantem a separação do tráfego da rede;
- Segurança e Controle de Acesso: ACLs, políticas de segurança e criptografia de dados.

#### Para-Virtualização

Técnica de virtualização que modifica o SO convidado para interagir diretamente com o hypervisor.
Seu funcionamento é baseado na modificação do kernel do guest OS para usar hypercalls com o uso de drivers virtuais para comunicação eficiente com o hypervisor.
Garante que as VMs só interajam com o hypervisor, nunca diretamente com o hardware ou outras VMs. Isso garante melhor desempenho e menos overhead, mas em compensação é necessário modificar o guest OS, limitando a compatibilidade.

#### Hypercalls

São interfaces de programação que permitem que o SO convidado faça chamadas diretamente para o hypervisor para realizar que operações necessitariam de acesso ao hardware físico.
Ele funciona substituindo syscalls direcionadas ao hardware por hypercalls ao hypervisor, que executa as chamadas ao hardware físico.

##### Prós do uso de Hypercalls

- **Melhor desempenho**
- **Menor overhead** 
- **Comunicação direta** entre o SO e o hypervisor, facilitando operações.

##### Contras do uso de Hypercalls

- **Necessidade de modificação no SO guest**, que limita alguns SOs que não suportam tal tecnologia;
- **Dependência do Hypervisor** específico do SO guest, limitando portabilidade e flexibilidade.

#### A questão da arquitetura de hardware

**Como a arquitetura de hardware afeta a virtualização**:
- **Execução de código nativo** permite execução direta na CPU;
- **Impacto de arquiteturas diferentes**: arquiteturas diferentes implicam em emulação, introduzindo sobrecarga de desempenho;
- **Compatibilidade e emulação** ineficiente.

#### Compatibilidade de Arquitetura na Virtualização

- Arquitetura de hardware: conjunto de instruções e design que define a capacidade de um processador.
- Dependência de arquitetura em VMs: o guest OS deve ser compilado para a mesma arquitetura do hardware físico para evitar a necessidade de emulação de instruções

Vantagens:
- Desempenho elevado;
- Menor overhead;
- Execução direta no hardware.

Limitações:
- Redução de flexibilidade;
- Restrições de compatibilidade entre SO e hardware.

#### Tópicos que podem ser impactados pela arquitetura na virtualização

##### Independência de Hardware

**Capacidade de mover VMs entre diferentes hosts físicos sem reconfiguração** obrigatória, facilitando a manutenção, atualizações e recuperação de desastres.
A independência de hardware não compromete o isolamento entre VMs mesmo quando são migradas entre hosts.

##### Server Consolidation

Técnica de **executar múltiplas VMs em um único servidor físico** para maximizar a utilização de hardware, reduzindo custos com hardware e energia, garantindo isolamento pelo hypervisor.

#### Funções Avançadas de Virtualização

##### Snapshots

Captura **estado atual da VM**, incluindo estado da memória, discos virtuais e configurações he hardware. São utilizados para **criar ponto s de recuperação** antes de atualizações ou mudanças críticas, permitindo uma restauranção rápida ao estado anterior em caso de falhas e testes.

##### vMotion

Tecnologia que permite a **migração ao vivo de uma VM de um host físico para outro sem interrupção de serviço** transferindo o estado da memória e configurações da VM de um host para outro, mantendo a continuidade das operações, melhorando o balanceamento de carga e facilitando a manutenção.

> A ideia de funcionamento é baseada na sincronização entre VMs de diferentes hosts. Inicialmente ocorre um processo de cópia de memória. Como a máquina continua executando, ao fim do processo de cópia, existe um passo de atualização de dados alterados, uma pausa breve da VM inicial e transferência de estado final para a nova VM. O ponto chave é que a nova VM terá a mesma configuração de rede, a infraestrutura só deve alterar em qual dispositivo físico o MAC Address está localizado.

##### High Avaiability (HA)

Configuração que permite o **reinício automático de VMs em outros hosts em caso de falha do hardware** através de DRS (Distributed Resource Scheduler), uma ferramenta de **balanceamento de carga de trabalho automática entre hosts em um cluster** para otimização de recursos. Proporcional tolerância a falhas completa para VMs críticas, criando uma réplica em tempo real em um segundo host.

> A ideia aqui é uma detecção de falhas + reinicialização em outro host do cluster. Diferente do vMotion, não é uma migração ao vivo, logo não da pra copiar o estado atual da RAM gerando um periodo de indisponibilidade.

> DRS → decide onde as VMs devem ficar para equilibrar recursos.
> vMotion → é o mecanismo que move a VM ligada de um host para outro.
> HA → reage quando um host falha, reiniciando suas VMs em outro host.
> FT → mantém uma réplica da VM em execução simultaneamente em outro host.
#### Desafios na Virtualização de Servidores

- **Compatibilidade de hardware**
- **Segurança**
- **Gerenciamento de recursos**
- **Isolamento de desempenho**
# Cloud

## Segregação e Compartilhamento MultiTenancy

Criar grupos na aplicação segregados de forma que um não enxerga o outro.
Exemplo: endereço de e-mail em @puc-campinas.edu.br e @ibm.com, a busca por um usuário na PUC não deve encontrar o usuário da plataforma IBM.
Como: Utilizar o domínio de acesso (@puc-campinas.edu.br) como tag relativa ao usuário e todas as requisições buscar pelo user e tag. Nesse formato de multitenancy não é necessário segregar bancos de dados, podendo utilizar apenas o SQL para segregar com base na tag.

### O que é MultiTenancy

Definição: arquitetura de aplicação onde uma unica instancia atende a míltiplos usuários, chamados tenants (inquilinos) que compartilham os mesmos recursos fisicos ou lógicos.

Isolamento de tenants: cada tenant usa a plicação como se fosse única, com a capacidade de personalizar a interface e fluxos de trabalho. A segurança é garantida através de mecanismos de isolamento de dados, autenticação e criptografia.

Essencial para o modelo SaaS.

### Vantagens

### Desafios

- **Segurança e isolamento**
- **Personalização por tentant**: a necessidade de permitir que cada tenant personalize o sistema sem interferir nos outros aumenta a complexidade
- **Gerenciamento de performance**: uso equilibrado de recursos por tenant para **não afetar o uso dos outros**
    - Se cada tenant for um processo, identifica cada um em um cgroup e limita o uso de cpus
    - Se um processo tem múltiplas threads com cada tenant, a solução é separar os domínios e contabilizar o uso user+tag e limitar a nível de software o uso da aplicação.
- **Backup e recuperação**: implementar processos de backup e recuperação separados por tenant

### Diferenças entre MultiTenancy e Virtualização

Multitenancy: uma única instância da aplicação atende múltiplos tentants isolados lógicamente mas compartilhando recursos
Virtualização: múltiplas instâncias virtuais de servidores operam em uma única máquina física, cada uma funcionando como um ambiente separado com seu próprio sistema operacional
Comparação: a virtualização ---- nao terminei [x]

### Pulou muitos slides

### Orquestração de MultiTenancy em Núvem Pública

- **Compartilhamento de Infraestrutura**: em uma cloud pública, os recursos de computação, armazenamento e rede são compartilhados entre vários tenants.
- **Elasticidade**: recursos como processamento e armazenamento são provisionados dinamicamente, com ajuste automático conforme a demanda de cada tenant aumenta ou diminui
- **Gerenciamento de Containers** tecnologias como kubernetes ajudam a isolar e gerenciar containers dedicados a cada tenant, compartilhando o mesmo hardware
- **Balanceamento de Carga**: serviços como o Elastic Load Balancing (AWS) garantem que as requisições de cada tenant sejam distribuídas eficientemente entre os recursos disponíveis

### Gerenciamento de recursos e performance

#### Isolamento de containers ou VMS

**Containers**: muitos ambientes multitenant usam containers ou vms para isolar os tenants. Cada container pode ter recursos (CPU, memória, etc) limitados, evitando que um tenant ultrapasse seu consumo permitido. Neste caso, temos um ambiente multi-instância, sendo uma instância para cada tenant.

#### Mecanismos de Rate Limiting

**Controle de chamadas e requisições**: limitar o número de requisições que um etnant pode fazer em determinado período de tempo. Isso impede que um tenant com alto volume de solicitações sobrecarregue o sistema.

#### Monitoramento de AutoScaling

#### Política de Penalização

Penalização de tenants de alto consumo: se um tenant ultrapassa o consumo de recursos permitido de forma recorrente, ele pode ser penalizado por meio de throttling (diminuição intencional de desempenho) ou movido para um ambiente de menor prioridade

### Gerenciamento de Identidade e Contexto do Tenant

- Identificador de tenant
- login e autenticação
- Carregamento de dados e configurações
- Ambientes independentes

### Modelos de Armazenamento de Dados em MultiTenancy

- **Banco de dados comparitlhado com esquemas compartilhados**: tenants compartilham as mesmas tabelas com consultas filtradas pelo ID do tenant, garantindo menor custo e eficiência de recursos, mas aumentando a complexidade em segurança
- **Banco de dados compartilhado com esquemas separados**
- **Banco de dados separado**

### Segurança e controle de acesso em multitenant

- Autenticação e autorização baseada em tenant: o sistema de controle de acesso verifica o tenant e ajusta as permissões conforme necessário
- RBAC (Role Based Access Controll): permissões definidas por papéis internos a cada tenant
- Filtragem de Requisições: 
- Criptografia

### Perdi aqui

### Elasticidade e Segurança
## Containers e cgroups

### O que são containers?

Containers são unidades de software que empacotam código e suas dependências, permitindo que as aplicações sejam executadas de maneira isolada e consistente em qualquer ambiente.
Diferente de VMs, os **containers compartilham o mesmo kernel do SO**, mas mantendo isolamento entre as aplicações, diretórios e runtime.
Permitem que o software seja portado de um ambiente para o outro (dev, homolog e prod) sem necessidade de ajustes no código.

### Diferenças entre containers e VMs

Containers:
- Compartilham o kernel do SO
- Leves com consumo reduzido de memória e recursos
- Iniciam rapidamente

VMs:
- Executam seu próprio SO
- Mais pesadas, consumindo mais recursos
- Inicialização lenta devido ao carregamento do SO

![Containers vs VMs](assets/containers-vs-virtual-machines.webp)

### Componentes de um container

- **Imagem**: Um container é criado a partir de uma imagem, que contém o código da aplicação, bibliotecas e demais configurações necessárias para execução. 
- **Registro de Imagens**: Imagens salvas em registros de containers que facilitam download e implantação.
- **Runtime de container**: Software responsável por executar e gerenciar containers, como o Docker e o containerd.
- **Isolamento de recursos**: O isolamento é estabelecido a tempo de execução pelo kernel e pelo runtime através de mecanismos como namespaces e cgroups.

### Isolamento de containers: Namespaces

Namespaces são uma **tecnologia do kernel Linux que cria um ambiente isolado para diferentes aspectos do SO**, como processos, rede e sistema de arquivos.
- **PID Namespace**: isola o espaço de identificação dos processos, de forma que cada container vejam somente seus próprios processos.
- **Net Namespace**: Isola interfaces de rede, IPs e roteamento, para que cada container tenha sua própria rede virtual.
- **Mount Namespace**: Isola o sistema de arquivos, criando uma visão separada dos pontos de montagem.
- **IPC Namespace**: Isola mecanismos de comunicação entre processos, como memoria compartilhada, semáforos e filas de mensagens. Sinais entre processos não são isolados pelo IPC Namespace.

### Isolamento de containers: cgroups

Os Control Groups (cgroups v2) são uma **funcionalidade unificada do kernel Linux que permite limitar, isolar e monitorar o uso de recursos por grupos de processos**, adotando uma hierarquia única com controle consistente e integrado de recursos. O objetivo é **garantir que um container não consuma todos os recursos e afete o desempenho do outro**. 
Recursos controlados:
- **CPU**: limita o tempo de processamento que cada container pode consumir;
- **RAM**: limita a quantidade de memória cada container pode utilizar;
- **I/O**: controla o acesso ao sistema de arquivos e dispositivos de armazenamento

O acesso é feito através do filesystem do Linux através do diretório `/sys/fs/cgroup/{nome do cgroup}`, sendo necessário a criação de arquivos relativos a cada uma das configurações disponíveis, como `cpu.weight`, `cpu.max`, `cpu.mems`, `cgroup.procs`, `cpuset.cpus` entre outros.

### Controlando o uso de CPU com cgroups

#### CPU Weight

Define uma **proporção do tempo de CPU que um container pode usar** em comparação com outros. Isso não limita estritamente o uso, mas prioriza o container em momentos de concorrência.

```sh
echo 100 > /sys/fs/cgroup/group_1/cpu.weight
echo 200 > /sys/fs/cgroup/group_2/cpu.weight
```

O container presente no group_1 possui o dobro de tempo de CPU que um container no group_2.

#### CPU Max

Limita a **quantidade absoluta de tempo de CPU que um container pode usar**. Esse limite é aplicado dentro de um período de tempo em microsegundos.

```sh
echo "50000 100000" > /sys/fs/cgroup/group_1/cpu.max
```

No exemplo acima, o group_1 pode usar até 50.000µs de CPU a cada período de 100.000µs, ou seja, no máximo 50% do tempo da CPU.

#### CPU Pinning

Permite restringir quais CPUs podem ser usadas pelos processos de um cgroup. O `cpuset.cpus` define as CPUs permitidas mas não garante exclusividade, apenas força que ela não saia dele. Essa técnica é útil para previsibilidade, controle de concorrência e melhor uso de cache.

```sh
echo 0-1 > /sys/fs/cgroup/group_1/cpuset.cpus
```

No exemplo acima restringe apenas o uso dos núcleos 0 e 1 da CPU para o group_1.

Mas como forçar exclusividade da CPU? Para tal feito, é necessário remover o núcleo do escalonador no boot através do parâmetro [isolcpus](#o-que-é-isolcpus).

#### Exemplos de uso

```sh
# Montar o cgroups v2
mount -t cgroup2 none /sys/fs/cgroup

# Criar um novo grupo
mkdir /sys/fs/cgroup/group_1

# Limitar o uso de CPU a 50% de 1 núcleo
echo "50000 100000" > /sys/fs/cgroup/group_1/cpu.max

# Adicionar processo ao cgroup
echo <PID> > /sys/fs/cgroup/group_1/cgroup.procs

# Definir prioridade relativa (opcional caso seja o único grupo a usar esta CPU)
echo 100 > /sys/fs/cgroup/group_1/cpu.weight

# Remover o group após o uso (apenas se não houverem processos rodando no cgroup)
rmdir /sys/fs/cgroup/group_1
```

#### Quando usar `cpu.max` e `cpu.weight`

[...]
`cpu.max` define limites "hard" de uso de CPU,  enquanto `cpu.weight` define prioridade de alocação em recursos de concorrência

```sh
# Exemplo 1:
mkdir /sys/fs/cgroup/my_group1
mkdir /sys/fs/cgroup/my_group2
echo "40000 100000" > /sys/fs/cgroup/my_group1/cpu.max
echo "40000 100000" > /sys/fs/cgroup/my_group2/cpu.max
echo 256 > /sys/fs/cgroup/my_group1/cpu.weight
echo 1024 > /sys/fs/cgroup/my_group2/cpu.weight
```

```sh
# Exemplo 2:
mkdir /sys/fs/cgroup/my_group1
mkdir /sys/fs/cgroup/my_group2
echo "max 100000" > /sys/fs/cgroup/my_group1/cpu.max
echo "max 100000" > /sys/fs/cgroup/my_group2/cpu.max
echo 256 > /sys/fs/cgroup/my_group1/cpu.weight
echo 1024 > /sys/fs/cgroup/my_group2/cpu.weight
```

#### CPU Pinning: Definindo em qual CPU um determinado cgroup será executado

[...] nao entendi
```sh
mkdir /sys/fs/cgroup/my_group1
mkdir /sys/fs/cgroup/my_group2

echo 0 > /sys/fs/cgroup/my_group1/cpuset.cpus
echo 0 > /sys/fs/cgroup/my_group2/cpuset.cpus

echo 0 > /sys/fs/cgroup/my_group1/cpuset.mems
echo 0 > /sys/fs/cgroup/my_group2/cpuset.mems

echo "100000 100000" > /sys/fs/cgroup/my_group1/cpu.max
echo "100000 100000" > /sys/fs/cgroup/my_group2/cpu.max

echo 256 > /sys/fs/cgroup/my_group1/cpu.weight
echo 1024 > /sys/fs/cgroup/my_group2/cpu.weight

echo $PID1 > /sys/fs/cgroup/my_group1/cgroup.procs
echo $PID2 > /sys/fs/cgroup/my_group2/cgroup.procs
```

#### Controlando o uso de memória com cgroups

##### Limite de Memória

O parâmetro `memory.max` define a **quantidade máxima de memória RAM que um grupo de processos pode utilizar**. Caso o limite seja ultrapassado, o kernel pode finalizar processos dentro do grupo para liberar memória (via [OOM Killer](#oom-killer-out-of-memory-killer))

```sh
echo 536870912 > /sys/fs/cgroup/group_1/memory.max # 512 MiB em bytes
```

No exemplo acima limitamos o group_1 com 512MB de memória.

##### Swap

Além da RAM, é possível limitar o uso de swap (memória trocada pra disco) através de `memory.swap.max`.

```sh
echo 0 > /sys/fs/cgroup/group_1/memory.swap.max
```

No exemplo acima impedimos o group_1 de utilizar swap, forçando a execução em RAM para evitar queda no desempenho.

##### Pinning de Memória

O parâmetro `cpuset.mems` permite definir quais nós [NUMA](#arquitetura-numa-non-uniform-memory-access) podem fornecer memória aos processos do cgroup.
Não é obrigatório definir o parâmetro em todos os cgroups: quando está vazio, os nós podem ser herdados do cgroup ancestral.
O arquivo `cpuset.mems.effective` mostra os nós de memória efetivamente disponíveis para o grupo.

#### O que é `taskset`

O taskset é uma ferramente CLI usada para **consultar ou alterar a afinidade de CPU de um processo**, permitindo dizer ao kernel Linux **quais CPUs lógicas um programa pode executar**.

```sh
taskset -c 7 ./meu_programa # inicia meu_programa permitindo execução somente na CPU 7

taskset -cp 7 PID # para alterar um processo já em execução

taskset -cp PID # para consultar a afinidade
```

**O taskset não reserva uma CPU. Se ela não estiver isolada, outros processos do sistema ainda podem ser escalonados nela.**

#### O que é `isolcpus`

É um parâmetro passado ao kernel durante o boot que remove CPUs específicas do escalonador de processos, deixando de distribuir tarefas comuns para elas. 
Neste cenário, para que ela seja usado é necessário definição explicita por meio de mecanismos de afinidade como `taskset` ou `cpuset.cpus`.
No entanto, ele não torna a CPU completamente livre de atividades do kernel, uma vez que interrupções e algumas tarefas internas ainda podem ser executadas nela.

##### Configurando `isolcpus` no GRUB

Em distribuições baseadas em Debian/Ubuntu:
```sh
vi nano /etc/default/grup

# Altere a linha
GRUB_CMDLINE_LINUX_DEFAULT="quiet isolcpus=7"

# Atualizar o GRUB
sudo update-grub
sudo reboot

# Confirmação
cat /proc/cmdline
```

#### Arquitetura NUMA (Non-Uniform Memory Access)

Sistemas com arquitetura NUMA possuem múltiplos nós de memória, cada um fisicamente mais próximo de certas CPUs. Uma vez que o acesso local à memória mais próxima da CPU é mais rápido, ao fazer o pinning é essencial escolher o nó com maior afinidade para garantir desempenho máximo.
Equipamentos com essa arquitetura são encontrados em servidores de data center e workstations de alto desempenho que possuem múltiplos sockets físicos de CPU. Notebooks e desktops convencionais normalmente possuem um único socket e são apresentados ao SO como um único nó NUMA (apesar de haver dispositivos modernos que possuem múlitplos nós dentro de um mesmo socket). Além disso, a complexidade e a latência de software exigida pela arquitetura acabam sendo um fator desgastante, uma vez que a arquitetura UMA (Uniform Memory Access) oferece baixa latência sem tanta complexidade.

##### Como descobrir qual nó de memória utilizar

```sh
numactl --hardware
lscpu --extend=NODE,CPU
```

##### Como amarrar CPU e memória

```sh
# CPU Pinning
echo 0 > /sys/fs/cgroup/group_1/cpuset.cpus
echo 0 > /sys/fs/cgroup/group_2/cpuset.cpus

# Definir nós compatíveis com as CPUs
echo 0 > /sys/fs/cgroup/group_1/cpuset.mems
echo 0 > /sys/fs/cgroup/group_2/cpuset.mems

# Definir uso máximo de CPU (100% de 1 núcleo)
echo "100000 100000" > /sys/fs/cgroup/group_1/cpu.max
echo "100000 100000" > /sys/fs/cgroup/group_2/cpu.max

# Prioridade relativa de CPU
echo 256 > /sys/fs/cgroup/group_1/cpu.weight
echo 1024 > /sys/fs/cgroup/group_2/cpu.weight
```

#### Prevenção de Exaustão de Recursos

##### OOM Killer (Out of Memory Killer)

Quando um cgroup excede o limite de memória definido, o kernel pode matar processos do grupo para liberar memória, garantindo que o sistema continue funcionando corretamente mesmo que os processos de um grupo tenha falhado ao gerenciar seu uso de memória

##### Rate Limiting para I/O

O cgroups v2 usa `io.max` para limitar a taxa de leitura e escrita de dispositivos de bloco (discos, SDDs, etc) evitando que um grupo monopolize o acesso ao armazenamento.
Por exemplo limitar a taxa de leitura para 10MB/s no device /dev/sda
```sh
echo "8:0 rbps=10485760" > /sys/fs/cgroup/my_container/io.max
```

###### Como saber qual é a identificação do container

```sh
lsblk -o NAME,MAJ:MIN
```

Onde no exemplo anterior, 8 é major, 0 é min (8:0)

### Docker containers

#### Execução de um container pronto

[...]

#### Modificando e salvando um container com `docker commit`

[...]

#### `Dockerfile`

[...]

#### Storage com Docker

O Docker oferece três maneiras de se trabalhar com storage, sendo abordagens úteis em diferentes cenários, seja para compartilhar arquivos entre o container e o host, como para **garantir que os dados sejam armazenados fora do ciclo de vida do container**

##### Volumes

Uma solução externa ao sistema de arquivos de container, armazenados de forma independente e gerenciados pelo Docker. Eles garantem que os dados persistam mesmo que o container seja removido. Neste cenário, é o ideal para **persistência de dados a longo prazo**.

Vantagens:
- **Compartilhamento entre múltiplos containers**;
- **Independentes**, armazenados fora do diretório e gerenciados pelo Docker;
- **Não dependem da estrutura do sistema de arquivos do host, facilitando migrações**

```sh
docker volume create meu_volume
docker run -d -v meu_volume:/usr/share/nginx/html nginx
```

##### Bind mounts

Uma solução para mapear diretórios ou arquivos do host diretamente no container. Ao contrário de volumes, dependem da estrutura de diretórios do host.

Vantangens:
- **Modificação em tempo real que refletem no container**
- Útil em ambientes de desenvolimento, onde **o código fonte pode ser editado diretamente no host**

```sh
docker run -d -p 8080:80 -v /meu_site:/usr/share/nginx/html nginx
```

##### tmpfs Mounts

Um tipo de armazenamento que usa a RAM para criar um sistema de arquivos temporários, não persistindo após o container/host ser parado ou reiniciado.

Vantagens:
- **Altamente rápido**, sendo ideal para dados temporários
- Mantém os dados em memória enquanto possível para acesso rápido, mas permite o uso de swap

```sh
docker run -d --name tmpfs_mount_example --tmpfs /app nginx # salva dentro de /app
```

#### Controlando o uso de recursos

[...]

#### Monitoramento e Logs

[...]

#### Desafios e boas práticas

[...]

#### Exercicio prático de controle de recursos

[...]
### Introdução a Kubernetes

Kubernetes parece ser muito complicado, mas ele traz muitas vantagens
Vamos usar o MiniKube

Containers facilitam a distribuição de aplicações empacotando o software completo que pode ser construída em uma imagem, executar como container e reproduzida em diferentes ambientes com maior previsibilidade.

Executar um único container é muito diferente de administrar centenas ou milhares deles. Em aplicações distribuídas surgem algumas perguntas:
- Qual servidor cada container deve executar?
- O que deve acontecer quando um container falha?
- Como redistribuir requisições?
- Como aumentar a quantidade de instâncias?
- Como realizar uma atualização sem interromper todo o serviço?

Kubernetes é frequentemente abreviado como K8s, é uma plataforma opensource desenvolvida pelo google destinada a execução e ao gerenciamento de aplicações conteinerizadas distribuidas em um conjunto de máquinas
Em vez de indicar manualmente qual servidor cada container deve executar, o administrador descreve o estado desejado da aplicação e o kubernetes executa as ações. Se declarar que uma aplicação deve ter 3 instâncias e uma delas cai, outra pode ser criada automaticamente.

### Cluster Kubernetes

Um ambiente Kubernetes é **organizado na forma de um cluster**, ou seja, um **conjunto de máquinas que cooperam para executar aplicações**.
O cluster possui duas grandes áreas funcionais (**dois nós**): o **Control Plane**, ou **Master Node**, responsável por **controlar e tomar decisões sobre o estado do ambiente**, e os **Worker Nodes**, responsáveis pela **execução efetiva das aplicações**.
Em ambientes de **produção**, encontramos **múltiplos nós e mecanismos de alta disponibilidade** para **reduzir a **possibilidade** de indisponibilidade** do cluster.

![Cluster Kubernetes](assets/cluster-kubernetes.png)

De forma resumida:
- Master Node: responsável por controlar e tomar decisões sobre o estado do ambiente
- API Server: 
- Scheduler: planejamento o que vai rodar e onde
- Controller Manager: quem executa as operações do scheduler
- etcd: database de estado

- Worker Node:
- `kubelet`: agente que roda no worker node (basicamente o kubernetes client, o que vai fazer o worker funcionar)
- `kube-proxy`: interface de rede entre os ambientes internos
- Container:
- Pod: container dentro de uma caixinha onde tem o container rodando e um endereço ip dele. ele não é um container puro pois normalmente não alocam um ip a ele, mas no pod obrigatoriamente sim. é possível rodar varios containeres dentro de um único pod
- Container Runtime: ambiente de execução do container

> Podemos compreender a arquitetura Kubernetes como uma **separação entre decisão e execução**: o **Control Plane determina o que deve ocorrer e os Worker Nodes executam as cargas de trabalho**.

### Control Plane

O control plane funciona como o **cérebro do cluster**. Ele **mantém informações sobre os recursos existentes, recebe comandos administrativos e decide quais ações devem ser executadas**.
Entre seus principais componentes estão: 
- `kube-apiserver`, que disponibiliza a Api Kubernetes. Grande parte das ações (em especial as executadas pelo comando `kubectl`) passam por uma solicitação para a API Kubernetes; 
- `etcd` utilizado para armazenar o estado do cluster;
- `kube-scheduler` responsável por decidir onde novos pods serão executados; 
- `kube-controller-mannager` que executa controladores responsáveis por manter o ambiente no estado desejado

### Worker Nodes

Os worker nodes são as **máquinas responsáveis pela execução das aplicações**. Cada Node disponibiliza recursos como CPU e memória. 
Entre seus principais componentes estão:
- `kubelet` que recebe instruções do Control Plane e verifica se os containers definidos para aquele nó estão realmente em execução;
- `container runtime`, responsável pela execução dos containers e componentes de rede;

### Kubernetes é orientado a objetos

Praticamente tudo é representado como um objeto da API.
Pod, Deployment, Service, ConfigMap, Secret e PersistentVolumeClaim são exemplos de objetos. Esses objetos são normalmente descritos por arquivos YAML

Exemplo de configuração (manifesto) de um Pod. Ele configura dinamicamente a configuração do IP
```yaml
apiVersion: v1
kind: Pod
metadata:
    name: examplo
spec: containers:
    - name: web
    image: nginx # Precisa estar no dockerhub
```

Tudo no kubernetes é temporário, ele é preparado pra recriar cenários dinamicamente. Nesse caso, dados persistentes NUNCA devem ser salvos no container/worker nodes. Devem ser salvos em volumes persistentes.

> **OBS AULA**: SWITCH SAM: Protocolo de rede para transferencia de dados de storage

### Estado desejado e reconciliação

Suponha que um Deployment declare:
- Estado desejado: 3 réplicas da aplicação
- Estado atual: 2 réplicas funcionando
Os controladores Kubernetes identificam essa diferença entre o estado desejado e o estado atual e procuram criar uma nova instância.

### Pod: a unidade básica de execução

O Pod é a **menor unidade de execução** gerenciada pelo Kubernetes
Um Pod contém **um ou mais containeres que compartilham determinados recursos**. Na maioria das aplicações, encontramos um container principal em cada Pod. Cada Pod pode ter IP e volumes associados.
Pods devem ser considerados **efêmeros**, isto é, se um Pod falhar, Kubernetes pode criar outro para substituí-lo. Neste caso, **não se projeta aplicações supondo que um Pod existirá permanentemente**. Ou seja, **dados não devem ser salvos em Pods**.

### Deployment e ReplicaSet

Deployment descreve **características de infraestrutura da aplicação**, como sua imagem, quantidade desejada de réplicas, formas de acesso, estratégia de atualizações, etc. Internamente, o Kubernetes **usa o ReplicaSets para manter o número apropriado de Pods em execução**.

**Se o Deployment declarar 3 réplicas e um Pod desaparecer, o controller cria outro** (mecanismo self-healing do Kubernetes). Deployments também permitem atualizações progressivas da aplicação.

ReplicaSet: conjunto de réplicas que vai usar em um determinado pod

### Manifestos do Kubernetes

#### Definição

É um **arquivo de definição usado para declarar recursos**, normalmente **escrito em YAML**, **descreve o estado desejado do recurso**.
```
kubectl apply -f manifesto.yaml
```

Exemplo de manifesto Deployment
```yaml
apiVersion: apps/v1
kind: Pod
metadata:
    name: minha-aplicacao
spec:
    replicas: 3
    selector:
        matchLabels: # todo mundo que tiver nessa aplicação vai usar isso
            app: minha-aplicação
    template:
        metadata:
            labels:
                app: minha-aplicacao
        spec:
            containers:
            - name: apache
              image: httpd
              ports:
              - containerPort: 80

```

### Labels e Selectors

Como Pods são recursos efêmeros, **aplicações não podem depender diretamente de atributos internos** como nome ou endereço IP. Para tal, Kubernetes utiliza **labels para identificar e organizar seus objetos**.
Um selector permite **localizar objetos que possuem determinadas labels**. **Deployments utilizam selectos para identificar seus Pods**, enquanto **Services utilizam o mesmo mencanismo para descobrir quais Pods devem encaminhar tráfego**.
O objeto **Service cria um acesso estável para um conjunto de Pods**, permitindo que as **instâncias sejam substituídas sem que os clientes precisem conhecer seus novos endereços**.

### E como criar um Service?

```yaml
apiVersion: v1
kind: Service
metadata:
    name: apache-service
spec:
    selector:
        app: apache
    ports:
        - port: 80
          targetPort: 80
    type: ClusterIP
```

O manifesto acima diz ao kubernetes criar um recurso do Tipo Service com o nome `apache-service`, selecionar os Pods com o label app `apache`, expor a porta 80 do Service e encaminhar para a porta 80 dos Pods além de utilizar o tipo ClusterIP.

Service não é acessado externamente pelos usuários, mas é algo interno.

### Tipos de Service e exposição da aplicação

O tipo **ClusterIP cria um endereço acessível apenas dentro do cluster** e é utilizado principalmente na **comunicação entre componentes da aplicação**.
O **NodePort disponibiliza o Service através de uma porta dos Nodes**. É simples e bastante utilizado em laboratórios. **Depende da exposição do IP do worker node ao ambiente externo** ao cluster.

ClusterIp (ip interno ao ambiente, não da pra acessar externamente) e Service são internos
NodePort -> porta externa

> Acesso ao IP de um worker node não acessa diretamente o worker, mas sim o Service, podendo cair em qualquer um dos Pods conectados.

```mermaid
flowchart TB
    client["Tráfego externo"]

    subgraph cluster["Kubernetes Cluster"]
        direction TB

        svc["Service"]

        subgraph workers["Worker Nodes"]
            direction LR

            subgraph worker1["Worker Node 1"]
                direction TB
                pod1["Pod"]
                pod2["Pod"]
            end

            subgraph worker2["Worker Node 2"]
                direction TB
                pod3["Pod"]
                pod4["Pod"]
            end

            subgraph worker3["Worker Node 3"]
                direction TB
                pod5["Pod"]
                pod6["Pod"]
            end
        end

        svc --> pod1
        svc --> pod2
        svc --> pod3
        svc --> pod4
        svc --> pod5
        svc --> pod6
    end

    client --> svc

    style cluster fill:none,stroke:#000,stroke-width:3px
    style workers fill:none,stroke:none
    style worker1 fill:none,stroke:#000,stroke-width:2px
    style worker2 fill:none,stroke:#000,stroke-width:2px
    style worker3 fill:none,stroke:#000,stroke-width:2px
```

### Formas de acesso externo ao cluster

#### Service type LoadBalancer

Solicita a infraestrutura (em ambiente de cloud gerenciado) um **Load Balancer externo associado ao Service**. Basicamente solicita a AWS para criar o LB.
O cliente **acessa um IP ou DNS externo fornecido pelo LB**, mas **internamente o Service possui um ClusterIP**. Dependendo da implementação, o LB pode usar NodePort como mecanismo interno de encaminhamento

#### Load Balancer Externo

**Um equipamento ou software externo ao Kubernetes para encaminhar tráfego para os Worker Nodes**, como Nginx ou outros LBs.
Normalmente encaminha o tráfego para portas do NotePort do cluster.

#### Ingress


**Permite centralizar o acesso HTTP/HTTPS a múltiplos Services do cluster**. Funciona como um **ponto único de entrada** para aplicações web. Utiliza regras de roteamento baseadas em:
```
Hostname: app1.exmeplo.com, app2.exemplo.com
URL Path: /api, /login
```
O Ingress **não encaminha diretamente para Pods**; ele **encaminha para Services, que então direcionam o tráfego aos Pods**.
**Requer um Ingress Controller instalado no cluster**, como NGINX Ingress Controller ou HAProxy Ingress
O **Ingress Controller** é quem efetivamente **recebe as conexões HTTP/HTTPS e aplica as regras definidas nos objetos** Ingress. Pode realizar também:
- Terminação TLS/HTTPS
- Redirecionamento HTTP -> HTTPS
- Balanceamento de carga entre os Pods através dos Services

Proxy Reverso dentro do ambiente kubernetes e ele tem acesso externo

### Persistência: Volumes, PV e PVC

Containeres e Pods devem ser considerados **recursos descartáveis**. **Dados importantes não devem ficar armazenados dentro deles.**
Kubernetes utiliza **Volumes para disponibilizar armazenamento aos Pods**. Quando o armazenamento precisa persistir, são utilizados **abstrações como o PersistentVolume (PV) e PersistentVolumeClaim (PVC)**.
O **PV representa armazenamento disponibilizado ao cluster**, enquanto o **PVC representa uma solicitação de armazenamento realizada pela aplicação**.

### Scheduling e distribuição dos Pods

Quando um Pod é criado, o **Scheduler precisa decidir em qual Worker Node ele será executado**. Essa decisão considera **recursos disponíveis e as restrições definidas para a aplicação**.
Também é possível **configurar regras para distribuir réplicas entre diferentes Nodes ou zonas, reduzindo a possibilidade de uma única falha interromper todas as instâncias** (como Pod Anti-Affinity)

### Minikube: Kubernetes local para laboratório

[...] mucho texto ignorei

a ideia é que o kubernetes deve ser executado em múltiplas máquinas, enquanto o minikube consegue rodar na mesma maquina. pra migrar do minikube pro kubernetes não é tao complexo, teria q criar algumas coisas espeecificas como o Ingress Controller que o kubernetes original nao tem

### Como o Minikube se relaciona com a arquitetura Kubernetes

[...]

### Minikube como ambiente de experimentação

[...]

### Minikube Multi-Node: simulando um cluster distribuído

[...]
## Redes Virtuais, SDN, NFV e Fabric

Redes em cloud precisa ser flexivel (múltiplos ambientes internos de forma transparente), com menor latência 

### O que são redes virtuais?

- Redes virtuais são **abstrações lógicas construídas sobre uma infraestrutura física**.
- Elas permitem **criar, gerenciar e modificar redes sem a necessidade de existir um equipamento físico dedicado** para cada função.
- A infraestrutura física fornece conectividade, enquanto a rede virtual **define logicamente como os recursos devem se comunicar**.
- Exemplos incluem VLANs (Virtual Lan), redes overlay, VNets/VPCs em cloud e redes utilizadas por máquinas virtuais e conteineres.

### Benefícios das Redes Virtuais

- Escalabilidade: permitem o crescimento da infraestrutura de rede sem a necessidade de novos dispositivos físicos;
- Flexibilidade: novas topologias sem reconfiguração física da rede;
- Redução de custo: otimização de hardware;
- Gerenciamento Simplificado: administração centralizada e automatizada.

### O que é SDN (Software Defined Network)

- SDN é uma abordagem que permite centralizar e automatizar o controle e a configuração da rede.
- Em vez de configurar individualmente cada switch e roteador, o administrador ou uma aplicaçao pode definir políticas, topologias e requisitos de conectividade de forma centralizada.
- O controlador SDN traduz essas necessidades em configurações e regras que são aplicadas aos dispositivos da rede.
- Os switches e roteadores continuam executando o encaminhamento de tráfego utilizando suas interfaces, tablelas, VLANs, rotas, túneis e demais recursos.

![Exemplo de SDN](assets/exemplo-sdn.png)

> A ideia é entender como fazer uma conexão entre dois pontos de rede A -> A' sem atribuir roteamento dinâmico, uma vez que nesse formato os roteadores aprenderiam todas as rotas e poderia afetar a segurança na comunicação de redes externas.
> Através do SDN, insere a rota A -> A' e o sistema fica responsável por gerar as rotas diretamente com base na regra. No exemplo acima ele gera um roteamento estático, mas poderia ser dinâmico com instância para cada rede.

### Funcionamento do SDN

- **Visão centralizada**: o controlador mantém uma visão lógica da topologia, dos dispositivos e das políticas da rede;
- **Abstração**: administração da rede como um todo no lugar de configurar cada equipamento individualmente;
- **Programação dos Dispositivos**: o controlador usa APIs e protocolos para gerir configurações e regras nos switches e roteadores;
- **Encaminhamento Distríbuido**: encaminhamento de pacotes localmente utilizando regras e tabelas configurados após programação.

Exemplo: ao solicitar conectividade entre dois ambientes, o controlador pode identificar os equipamentos envolvidos e configurar automaticamente VLANs, VXLANs, interfaces, políticas ou rotas necessárias.

> Protocolo NETCONF: configurações em XML com RPC (Remote Procedure Call)

### Três camadas/planos da arquitetura sdn


- **Camada da aplicação**: 
- Plano de controle
- Plano de dados

![Exemplo de SDN](assets/arquitetura-sdn.png)


### Vantagens do SDN

- Gerenciamento Centralizado
- Automação
- Escalabilidade
- Maior visibilidade: visão ampla da topologia, dispositivos e politicas
- Agilidade: mudanças implementadas mais rapidamente

### Casos de Uso do SDN

- Redes em Data Centers (mais usado): provisionamento ágil de redes para novos servidores ou VMs, automatizando a criação e gestão de redes overlay e VLANs.
- Redes WAN (Wide Area Network, longa distância): otimizar o roteamento em grandes redes corporativas, melhorando a eficiência do tráfego entre filiais.
- Redes de Opereadoras: operadoras de telecomunicação podem utilizar para gerenciar redes móveis e fixas de forma mais eficiente e a prova de erros.

### Exemplos de Software e Hardware em SDN

[...] preguiça

### O que é NFV (Network Function Vritualization)?

- NFV é uma abordagem em que funções de rede tradicionalmente executadas por equipamentos dedicados passam a ser implementadas em software.
- Em vez de utilizar um equipamento físico específico para cada função, essas funções podem executar em servidores, máquinas virtuais ou outras plataformas computacionais.
- Exemplos de funções virtualizadas:
  - Firewall
  - Roteador / NAT
  - Proxy
  - IDS / IPS
  - Load Balancer
- NFV e SDN são tecnologias independentes, mas podem ser utilizadas em conjunto para aumentar a automação e a flexibilidade da infraestrutura


```sh
echo "1" > /proc/sys/net/ipv4/ip_forward
sudo apt-get install zebra # roteamento

# Modulo do kernel NETFILTER para firewall
```
Transformar um linux em roteador

### Benefícios do NFV

[...] terminar de copiar

- Redução de custos
- Escalabilidade Dinâmica
- Implantação Rápida
- Automação

Pra que colocar tanta caixa de dispositivo de rede se o linux faz tudo? tudo virtual

### Casos de uso do NFV

[...]

- Operadoras de telecomunicação
- Firewalls e segurança
- SD-WAN

### Management and Orchestration

[...]

### O que é Fabric de Rede?

- Uma Network Fabric é uma arquitetura de rede em malha projetada para oferecer conectividade uniforme entre os dispositivos.
- Ela utiliza múltiplos caminhos entre os elementos da rede, aumentando escalabilidade, disponibilidade e previsibilidade.
- Em data centers, uma implementação comum é a arquitetura **Leaf-Spine**. Nessa arquitetura, cada switch Leaf conecta-se aos switches Spine, permitindo múltiplos caminhos entre servidores e serviços.
- Esse modelo é especialmente adequado para o tráfego **East-West**, comum em ambientes de data center e cloud.

[...] foto as 8h58 do tablet do ximenes

Prover conectividade de qualquer lugar da rede para qualquer lugar da rede sem perder latencia, só um hop
VX-LAN: encapsulamento sem usar trunk (sem spanning-tree)

### Tipos de Fabrics de Rede

[...]

### Como SDN, NFV e Fabrics trabalham juntos?

- Fabric: fornece a infraestrutura de conectividade física ou virtual pela qual o tráfego é transportado.
- SDN: Centraliza e automatiza o controle, as políticas e a configuração da rede.
- NFV: Implementa funções de rede em software, como firewalls, roteadores e balanceadores.

Exemplo: [...]

BGP transporta informações

### 
# Cloud

## Introducao

Leaf-spine: totalmente camada 3 (roteado, todas as interfaces tem roteamento IP [não existe switch nesta camada], todo leaf é conectado a todos os spines)

ECMP : Equal cost multipath - balanceamento de carga para caminhos de mesmo custo

caracteristicas do leaf-spine
- qualquer maquina chega a qualquer maquina com 1 hop somente
- multiplos caminhos permitem implementar ECMP
- ausencia de spanning tree (STP, ele remove os multiplos caminhos, impossibilitando LB)
- trafego em qualquer direção

rede hierarquica: trafego em funil, no leaf-spine pode ser em qq fluxo



/28 -> 16 endereços -> 14 alocaveis(endereço de rede e broadcast)
/29 -> 8 endereços -> 6 alocaveis
/30 -> 4 endereços -> 2 alocaveis
/31 -> 2 endereços -> 0 alocaveis

no leaf-spine como cada dispositivo deve estar conectado com todos os outros, colocar /30 ia gerar muitas redes e desperdiçar 50% da rede com broadcast e end. rede. Para facilitar isso, optaram que para conexao ponto a ponto, é possível alocar /31 2 dispositivos (switches em camada 3), descartando rede e broadcast. Isso garante uma maior eficiencia na rede.
cada switch vai ter um ip de gerenciamento e cada interface vai ter uma rede /31

## Tópicos avançados de redes para datacener

BGP
Virtual Extensible Lan
Ethernet VPN

## Da Fabric para BGP e VXLAN

OSPF: menor caminho disponivel com menor custo
BGP: nao prioriza menor caminho ou latencia, os primeiros atributos para calcular é as politicas de roteamento da rede. Altamente customizado, politicas de roteamento que podem ser gerenciadas concorrentemente. 
Utilizado em ambiente de fabric devido suas capacidades, visto que ele tem capacidade de criar suas adjacencias e trocar rotas (troca qq tipo de informacaø uma vez que os dispositivos estao todo sconectados)

## O que é BGP

é um protocolo de roteamento utilizado para trocar informações de alcançabilidade entre diferentes redes IP.

Diferente do OSPF, ele analisa "Quais AS Path (Autonomous System) a rota passa?"
- protocolo de roteamento mais utilizado na internet
- capacidade de trafegar nao somente rotas, mas tambem outros ambientes como backbones MPLS. basicamente a ideia é pegar uma rede grande e criar fluxos internos marcados com label para que não se misturem. ambientes de roteamento isolados, propagados via bgp. FOTO MIN 08:25

## eBGP e iBGP

eBGP: quando a sessão é estabelecida entre roteadores pertencentes a AS diferentes
iBGP: internal BGP: quando os roteadores pertencem ao mesmo AS

## Como uma sessão BGP funciona?

diferente do OSPF
OSPF: quando ativa o router ospf e sobe ele numa interface, ele joga broadcast na rede para identificar outros routes e tenta fazer autenticacao, se necessário. 
BGP: é necessário uma configuracao manual estabelecendo adjacencia de redes.
Foto min 08:28. No primeiro cenario nao tem a conexao direta entre os dois routers, eles estao em um switch e so de conectar e ligar o ospf ele ja funciona, enquanto no bgp é necessário entrar em cada router e criar a conexao -> isso da muito mais trabalho, mas garante mais segurança

## iBGP, Full Mesh e Route Reflector

em ibgp é necessário estabelecer um full mesh, conectar todos os roteadores diretamente, pois se não implementar ele vai entender que algumas rotas podem ter loop de roteamento e vai correr o risco de voltar nele mesmo e cortar o tráfego.
como solução tem o route reflector, que seria um roteador base e os demais replicam (similar ao designated router no ospf)

## BGP Route Reflector

no lugar de todos passarem rotas pra todso, eles mandam pro RR. deve ter um backup pra caso esse cara caia

## O que o BGP anuncia?

anuncia prefixos, a diferença é que os prefixos vem com algumas informacoes adicionais -> OSPF passa prefixo e hierarquia da rede, o BGP passa alem da topologia ele passa o AS Path pra cada um dos destinos. Pode passar mais informacoes pra definir a rota, o as path é um deles

## BGP é um protocolo de path vector

## Principais atributos do BGP

AS_PATH: lista de AS
NEXT_HOP: identifica o endereço ip do proximo roteador a ser utilizado
    Relativo a politica, ele utiliza arp request para identificar como chegar no caminho, pq o next_hop nao necessariamente esta diretamente conectado no bgp. similar a um next hop recursivo. Min 08:38
LOCAL_PREF: permite estabelecer perfêrencias de saída dentro de um AS

```mermaid
flowchart TD
    R[Roteador] -->|Rota A| S1[Serviço 1]
    R -->|Rota B| S2[Serviço 2]
    R -->|Rota C| S3[Serviço 3]   

    R{Roteador}

        %% Define Square Node (Router)
    Router[Router]
    
    %% Define Circle Node (Endpoint/Route)
    Endpoint((Server))
    
    %% Connect with Route
    Router -->|Route| Endpoint   
```

```mermaid
sequenceDiagram
    Client->>Roteador: Requisição
    Roteador->>Backend A: Rota /api/a
    Roteador->>Backend B: Rota /api/b   
```

## perdi aqui

## BGP vs. OSPF

## BGP em datacenters

Onde é usado em datacenter? comunicacao entre switches leaf-spine. cada um dos switches tem endereço virtual loop-back para gerenciar os switches. min 08:48 - nao entendi mais nada dessa parte

## Por que se faz isso? (Vantagens do eBGP)

## overlay e underlay

## Limitações das VLANs tradicionais

em um ambiente convencional de vlan é possível ate 4096 redes (12 bits), oq é suficiente pra maioria. Mas em um cenário de datacenter que precisa de muitas redes, vem o VXLAN que permite 24 bits, o equivalente a 16 milhoes de redes

## O que é VXLAN

## Encapsulamento VXLAN

Pega o frame ethernet com a tag de vlan e encapsula dentro da area de dados de um pacote iP (duas imagens no min 08:55)

VPN L2 Over L3 -> pacotes L2 encapsuladas em pacotes L3. a flexibilidade é tao grande que permite jogar ate pra outro datacenter

## VNI

Mapeamento de tag de vlan para um VNI. Todo cliente usa os mesmos nomes de VLAN (10,20,30,40), nisso o provedor pode pegar um range de por exemplo 100-200 e mapear para 10100-10200 vni. so que tem que ser manual, pra isso pode usar script em python pra automatizar esse processo.

# Lista para P1

## Lista de Exercícios

### Introdução, Funções e Tipos de Serviços, Tipos de Cloud, Responsabilidade Compartilhada e CMM

1. Uma empresa mantém servidores próprios que **permanecem ligados durante todo o ano**, embora sejam utilizados **intensamente apenas durante alguns períodos do mês**. Explique como a adoção de computação em nuvem poderia alterar a forma como essa empresa utiliza e paga pelos recursos computacionais. Relacione sua resposta a pelo menos duas características da computação em nuvem.
> Existem alguns pontos que poderiam alterar o uso dos recursos, como por exemplo:
> - **reducão do imposto**, uma vez que cloud é despesa e não investimento;
> - **escalabilidade e elasticidade**, permitindo reduzir ou aumentar recursos computacionais de forma automatica, seja em cenários de pico ou automatizados

2. Um sistema possui normalmente **quatro servidores**. Em determinados horários, a **utilização aumenta** e o ambiente passa automaticamente para **dez servidores**. Após o pico, **retorna para quatro**. Explique quais conceitos de escalabilidade e elasticidade estão presentes nesse cenário e por que eles não devem ser considerados exatamente a mesma coisa.
> O cenário apresenta conceitos de escalabilidade horizontal, uma vez que o sistema é capaz de aumentar sua capacidade de instâncias de servidor de 4 pra 10. Também apresenta conceitos de elasticidade, uma vez que essa quantidade de recursos é ajustada automaticamente conforme demanda. Os conceitos não são iguais porque escalabilidade representa a capacidade de um sistema aumentar seus recursos para suportar crescimento de carga, enquanto elasticidade envolve ajustar esses recursos dinamicamente, tanto para cima quanto para baixo, conforme a necessidade.

3. Uma empresa afirma que sua infraestrutura é “**flexível” porque consegue aumentar rapidamente a quantidade de servidores** quando há aumento de demanda. Analise criticamente essa afirmação. O exemplo apresentado demonstra necessariamente flexibilidade? Diferencie flexibilidade, escalabilidade e elasticidade utilizando esse cenário.
> Aumentar dinâmicamente servidores é uma forma de flexibilidade mas não necessariamente indica que a infraestrutura é flexível, uma vez este conceito é amplo. O comportamento indicado acima representa uma **escalabilidade horizontal**, pois possui a capacidade de acrescentar instâncias de servidor para suprir a demanda. Caso esse processo seja feito automaticamente sob demanda, também representa uma **elasticidade**. A flexibilidade por si só é um conceito mais amplo relacionado a capacidade da infraestrutura de se adaptar a configurações e necessidades, como modificar recursos, controle remoto entre outros. **Os três conceitos são relacionados mas não equivalentes**.
   
4. Uma organização pretende migrar para a nuvem exclusivamente porque **espera reduzir custos**. Entretanto, seus sistemas possuem **requisitos elevados de segurança**, **dependem de tecnologias proprietárias** e a equipe possui **pouca experiência com ambientes cloud**. Explique por que a decisão não deveria considerar apenas redução de custos. Identifique e analise três fatores de risco ou desafio que deveriam participar dessa decisão.
> A redução de custos infraestrutura não é o único fator que deve ser analisado durante uma migração pra cloud, deve-se analisar alguns outros, como por exemplo:
> - necessidade de **mão de obra especializada** para o provedor, o que não existe no cenário acima, sendo mais um custo;
> **dificuldade na migração** uma vez que dependem de tecnologias proprietárias e possivelmente **legadas**;
> **perda do controle direto sobre a infraestrutura física**, passando a operar em um modelo de **responsabilidade compartilhada**, abrindo brechas sobre dados sensíveis e segurança.

5. Clustering, Grid Computing e virtualização existiam antes da popularização da computação em nuvem. Explique de que maneira essas tecnologias contribuíram para tornar a cloud moderna possível, mas justifique também por que possuir virtualização, clusters ou um grid não significa, por si só, possuir um ambiente de computação em nuvem.
> Inicialmente, definirei o significado de cada uma delas:
> - Clustering: grupo de recursos de TI independentes e homogeneos interconectados atuando como um único sistema;
> - Grid: grupo de recursos de TI heterogeneos organizados em pools lógicos formando um supercomputador virtual;
> - Virtualização: criação de instâncias virtuais de recursos físicos de TI.
> 
> De forma geral, a criação dessas tecnologias implicou na capacidade de redução de hardware físico, além da implementação de termos como escalabilidade e resiliência, oferecendo uma plataforma robusta para aplicações de grande escala.
> Possuir esses cenários não implica em um ambiente de cloud uma vez que para ser considerado cloud é necessário implementar alguns conceitos específicos como escalabilidade, elasticidade, automação de processos, capacidade de configurar recursos sob demanda com o mínimo de integração com o provedor, etc.

5. Uma empresa utiliza o **Microsoft 365 para e-mail corporativo** e, ao mesmo tempo, mantém **máquinas virtuais** em um provedor de nuvem para executar um **sistema desenvolvido internamente**. Identifique qual dos dois serviços se aproxima de SaaS e qual se aproxima de IaaS, explicando o raciocínio utilizado.
> O Microsoft 365 como e-mail se aproxima de um SaaS, uma vez que é um software quase totalmente gerenciado por parte da Microsoft, cabendo ao usuário somente configurações e personalizações no lado da aplicação.
> O software desenvolvido internamente se aproxima de um IaaS, uma vez que o desenvolvedor precisa desenvolver o sistema internamente e lidar com a gestão interna da máquina virtual fornecida pelo provedor.

7. Uma empresa **desenvolve um sistema** e o **disponibiliza como serviço** para seus clientes, mas **executa esse sistema sobre a infraestrutura de outro provedor** de nuvem. Explique como essa mesma empresa pode assumir simultaneamente diferentes papéis no ecossistema cloud, como cloud consumer, cloud service owner e cloud provider.
> A empresa em questão é tanto consumidora da infraestrutura cloud fornecida pelo provedor, quanto provedora, fornecendo um SaaS em cloud para seus clientes. Quando é relativo a aplicação, a empresa possui a propriedade legal e responsabilidades sobre ele, se tornando service owner; quando é relativo a disponibilidade e infraestrutura, o provedor de cloud se torna o service owner.

8. Uma equipe de desenvolvimento precisa criar uma nova aplicação, mas **não deseja administrar sistemas operacionais**, aplicar patches na infraestrutura ou manter o ambiente de execução. Ao mesmo tempo, precisa **controlar completamente o código e os dados da aplicação**. Compare IaaS, PaaS e SaaS e justifique qual modelo de entrega melhor atende a esse cenário.
> IaaS: **locação de infraestrutura**, o consumidor é responsável por gerir completamente a máquina virtual locada e a aplicação, deixando como responsabilidade do provedor apenas a manutenção da máquina host. Neste caso não é uma boa escolha, uma vez que não deseja administrar a VM.
> SaaS: **locação de software**, o consumidor é responsável por gerir apenas seus dados e controles de personalização da aplicação. Uma vez que o objetivo é desenvolver o software como um todo, não é uma boa escolha.
> PaaS: **locação de plataforma de desenvolvimento**, o consumidor é responsável por desenvolver a aplicação, enquanto o provedor lida com atualizações tanto na máquina host quanto na VM, sendo a escolha ideal neste cenário. 

9. Uma organização **possui seus servidores internos**, mas utiliza também um **serviço de banco de dados gerenciado por um provedor externo**. Explique por que esse banco pode estar fora do organizational boundary da empresa e, ao mesmo tempo, dentro de seu trust boundary. O que a empresa deveria avaliar antes de incluí-lo nesse limite de confiança?
> **Organizational Boundary** representa a **fronteira física que limita quais recursos estão sobre sua propriedade e controle direto**. Uma vez que o banco de dados está em um provedor externo fora de seu controle direto, ele não está em seu organizational boundary.
> **Trust boundary** representa a **fronteira lógica que se estende para incluir recursos nos quais uma organização decide confiar**. Apesar de não ter seu controle direto, por possuir SLAs, a empresa decide confiar no ambiente e inclui-lo em seu trust boundary.

10. Uma empresa **Alpha desenvolve um sistema SaaS** e o vende para diversas empresas. O software é **executado em uma plataforma PaaS fornecida pela empresa Beta**. A **administração** das contas, usuários e configurações da aplicação é realizada por uma **terceira empresa, Gamma**. Os clientes finais acessam o sistema pela Internet. Analise o cenário e identifique, justificando:
    - quem atua como cloud provider e cloud consumer em cada relação;
    - quem é o service owner;
    - quem exerce funções de resource administrator;
    - como os organizational boundaries e trust boundaries podem ser diferentes para Alpha e para os clientes finais.
> [...]

11. Uma empresa possui um datacenter próprio com dezenas de servidores físicos e máquinas virtuais. Os recursos são provisionados manualmente pela equipe de TI mediante abertura de chamados. É correto afirmar que essa empresa possui uma nuvem privada apenas porque a infraestrutura pertence a ela? Justifique.
> Não é correto afirmar, uma vez que para ter uma nuvem privada é necessário que a infraestrutura tenha conceitos específicos que define a cloud, sendo um ambiente projetado para provisionamento remoto de recursos escaláveis, fornecendo mecanismos de escalabilidade, elasticidade, flexibilidade, resiliência, automação de processos, pay-as-you-go, multitenancy, acesso ubíquo.

12. Duas empresas utilizam exatamente os **mesmos serviços da AWS**. Cada uma possui suas próprias VNets/VPCs, regras de firewall, máquinas virtuais e bancos de dados, sem permitir acesso da outra aos seus recursos. O fato de cada empresa possuir um ambiente logicamente isolado transforma esses ambientes em nuvens privadas? Explique a diferença entre ambiente privado dentro de uma nuvem pública e nuvem privada.
> O fato de cada empresa possuir um ambiente logicamente isolado não transforma eles em nuvens privadas, uma vez que a infraestrutura física de nuvem não é exclusiva para sua organização, sendo uma nuvem pública com características de funcionamento virtualizadas e isoladas.

13. Um grupo de universidades deseja compartilhar uma infraestrutura de cloud para pesquisa científica. Todas possuem requisitos semelhantes de segurança e pretendem dividir custos, mas desejam também participar das decisões sobre regras de uso, expansão e acesso à infraestrutura. Explique por que uma nuvem comunitária poderia ser considerada nesse cenário e identifique o principal desafio de governança que provavelmente surgiria.
> Uma nuvem comunitária pode ser considerada boa uma vez que ela representa uma nuvem privativa por parte de um grupo de pessoas e/ou empresas para um fim específico em comum. O principal problema é a governança da nuvem, indicando quem irá administrar e ser responsável pelas decisões e quais decisões devem e podem ser tomadas.

14. Uma empresa mantém seus bancos de dados mais sensíveis em infraestrutura própria, mas utiliza recursos de uma nuvem pública para executar processamento adicional durante períodos de pico. Explique por que esse cenário pode ser caracterizado como nuvem híbrida e analise dois desafios técnicos necessários para que os ambientes funcionem de maneira integrada.
> Pode ser considerado nuvem hibrida uma vez que inclui a combinação de elementos de múltiplos tipos de nuvens (on-premise e pública). Os principais problemas incluem fazer os ambientes trabalharem em conjunto, em especial a sincronização e a conectividade entre os ambientes.

15. Uma instituição possui três requisitos:
    - determinados dados **não podem sair de sua infraestrutura própria**;
    - aplicações públicas precisam **crescer rapidamente durante picos** de utilização;
    - a instituição deseja utilizar **serviços de inteligência artificial oferecidos por dois provedores públicos** diferentes.

    Explique como uma arquitetura pode combinar nuvem privada, nuvem pública, nuvem híbrida e multicloud nesse cenário. Mostre claramente por que híbrida e multicloud não são sinônimos, mesmo podendo existir simultaneamente.
> A melhor abordagem seria uma nuvem híbrida e multicloud. Para garantir segurança, os dados são armazenados em nuvem privada e a as aplicações são replicadas na nuvem publica e na privada com link dedicado para reduzir latência, disponibilizadas através de proxy reverso com load balancer. Com relação aos serviços de IA, seria uma abordagem multicloud.
> Apesar de terem conceitos semelhantes, multicloud foca em redução da dependência entre fornecedores, enquanto a nuvem hibrida foca em alternar diferentes tipos de ambientes para garantir segurança e escalabilidade em diferentes cenários.

16.   Uma empresa migrou uma máquina virtual de seu datacenter para um serviço IaaS e passou a acreditar que não precisa mais atualizar o sistema operacional porque “agora o servidor está na nuvem”. Explique o erro dessa interpretação utilizando o conceito de responsabilidade compartilhada.
> Ao escolher um serviço do tipo IaaS, a responsabilidade do provedor passar ser garantir segurança e disponibilidade a nível de hardware. Parte da responsabilidade do cliente manter o sistema atualizado para garantir segurança a nível de SO.

17.   Compare IaaS, PaaS e SaaS do ponto de vista da responsabilidade do cliente. À medida que se passa de IaaS para PaaS e depois para SaaS, o que tende a acontecer com o controle e com a responsabilidade operacional do cliente? Explique utilizando exemplos de componentes da solução.

18.   Uma aplicação executada em PaaS sofreu uma invasão porque o desenvolvedor criou uma API sem autenticação adequada. O cliente afirma que o provedor deveria assumir a responsabilidade porque a aplicação estava hospedada na infraestrutura dele. Analise essa afirmação utilizando o modelo de responsabilidade compartilhada.
> O provedor é o responsável legal por lidar com a aplicação, enquanto o provedor é responsável por lidar com a infraestrutura de desenvolvimento. Como a autenticação é uma falha a nível de software, o cliente deve assumir as responsabilidades sobre a falha. 

19. **Estudo de caso:** Uma empresa utiliza um sistema financeiro SaaS. O fornecedor mantém o software atualizado, realiza backups da plataforma e protege sua infraestrutura. Um funcionário da empresa cliente recebe privilégios administrativos excessivos e exporta informações financeiras confidenciais.
Analise o incidente e explique:
    - quais controles estavam sob responsabilidade do provedor;
    - quais estavam sob responsabilidade do cliente;
    - por que utilizar SaaS não transfere toda a responsabilidade de segurança ao provedor.
> - As responsabilidades do provedor são relativos a garantir segurança, disponibilidade e funcionamento da **aplicação**.
> - Garantir privilégios corretos para cada subusuário na aplicação, além de usar a plataforma seguindo os termos do contrato.
> - Tem alguns cenários que complicam, como por exemplo: 
>   - Limitação na personalização caso o provedor seja responsável pela segurança total;
>   - Não garantir que o usuário utilizou a aplicação de forma correta (o que aconteceu)

20.  **Estudo de caso:** Uma empresa possui a seguinte arquitetura:
    - máquinas virtuais em IaaS executando sistemas legados;
    - uma nova aplicação desenvolvida em PaaS;
    - e-mail corporativo fornecido como SaaS.

    Após uma auditoria foram encontrados três problemas:

    1. o sistema operacional de uma VM não recebe patches há seis meses;
    2. a aplicação PaaS possui permissões excessivas no acesso ao banco de dados;
    3. uma conta administrativa do serviço de e-mail utiliza senha fraca e não possui controles adicionais de acesso.

    Para cada problema, identifique quem possui a responsabilidade principal — cliente ou provedor — e explique por que a divisão de responsabilidades muda entre os três casos. Ao final, explique por que a frase “quanto mais gerenciado é o serviço, menos responsabilidade o cliente possui” pode ser útil, mas também perigosa se interpretada de forma absoluta.
> 1 - A responsabilidade cabe ao cliente, que ao optar por um IaaS, tem como responsabilidade gerenciar o SO;
> 2 - Responsabilidade do cliente, visto que é uma falha da aplicação ter permissões excessivas no acesso ao banco de dados;
> 3 - Responsabilidade do cliente, uma vez que tem senha fraca e sem controle de acesso.
> 

1.   Duas empresas utilizam a mesma quantidade de máquinas virtuais em cloud. A empresa A cria e administra os recursos manualmente, sem políticas comuns. A empresa B possui processos padronizados, governança e monitoramento do ambiente. Explique por que a quantidade de recursos em cloud não é suficiente para determinar a maturidade das duas organizações.

2.   Uma empresa possui diversos departamentos utilizando serviços de nuvem de forma independente. Alguns utilizam IaaS, outros SaaS e alguns criaram ambientes de desenvolvimento sem conhecimento da área central de TI. Explique quais características desse cenário indicam um estágio inicial de maturidade e quais mudanças seriam necessárias para que a organização avançasse para um uso mais repetível e coordenado.

3.   **Estudo de caso:** Uma empresa apresenta as seguintes características:

    - utiliza cloud em praticamente todos os seus sistemas;
    - possui políticas centralizadas de segurança e governança;
    - os processos de implantação são definidos e repetíveis;
    - existe monitoramento dos ambientes;
    - porém métricas de custo, desempenho e eficiência ainda não são utilizadas sistematicamente para otimização.

    Com base no CMM apresentado em aula, indique em que região da escala de maturidade essa organização se encontra e justifique sua análise. Em seguida, explique quais mudanças seriam esperadas para que ela avançasse para o próximo nível.

4.  **Estudo de caso:** Uma grande organização realizou uma avaliação CMM e encontrou o seguinte cenário:

    - **Tecnologia:** alto nível de automação, IaC e CI/CD;
    - **Segurança:** políticas bem definidas e monitoramento contínuo;
    - **Finanças:** pouca visibilidade dos custos de cloud;
    - **Pessoas:** equipes com níveis muito diferentes de conhecimento;
    - **Processos:** algumas áreas seguem padrões corporativos, enquanto outras trabalham de forma independente.

    A diretoria concluiu que, como a tecnologia está avançada, a empresa deve ser classificada simplesmente como “nível 4”. Analise criticamente essa conclusão. Explique por que o CMM não deve ser interpretado apenas como uma nota única baseada na tecnologia e proponha como a organização deveria utilizar os resultados por domínio para construir um roadmap de evolução de maturidade.

### Bases Tecnológicas

1. Uma aplicação corporativa foi migrada de um datacenter local para a nuvem. Os servidores na nuvem possuem capacidade computacional superior aos servidores antigos, mas os usuários passaram a perceber maior demora na resposta da aplicação. Explique por que aumentar CPU e memória dos servidores pode não resolver o problema. Relacione sua resposta ao papel da rede no acesso a serviços em nuvem.
> Aumentar CPU e memória pode melhorar o tempo de processamento dos servidores, mas isso, por si só, não garante um menor tempo de resposta da aplicação. É possível que a região ou zona de disponibilidade escolhida na nuvem esteja geograficamente distante dos usuários finais, aumentando a latência da comunicação pela rede. Esse impacto pode ser ainda maior quando a aplicação realiza múltiplas comunicações entre serviços, APIs ou bancos de dados. Portanto, o desempenho da aplicação depende não apenas da capacidade computacional dos servidores, mas também das condições e da arquitetura da rede.

2. Uma videoconferência apresenta interrupções e falhas no áudio mesmo quando a conexão possui largura de banda aparentemente suficiente. Explique como latência, jitter e perda de pacotes podem provocar esse comportamento e por que largura de banda, isoladamente, não é uma medida suficiente da qualidade da conexão.
> Latência corresponde ao tempo que um pacote leva para ir de um ponto a outro; jitter é a variação dessa latência ao longo do tempo; e perda de pacotes ocorre quando alguns pacotes enviados não chegam ao destino, podendo ser descartados por congestionamento, falhas de transmissão ou outros problemas na rede.
> Em videoconferências e outros cenários sensíveis ao tempo, essas métricas são essenciais para avaliar a qualidade da comunicação. Uma latência elevada provoca atrasos na conversa e prejudica a sensação de tempo real; jitter elevado faz com que os pacotes cheguem em intervalos irregulares, podendo causar travamentos e distorções no áudio ou vídeo; e a perda de pacotes pode provocar cortes, falhas momentâneas ou degradação da qualidade.
> A largura de banda indica apenas a capacidade de transmissão da conexão, mas não garante que os dados cheguem rapidamente, de forma regular e sem perdas.

3. Uma empresa acessa seus serviços em nuvem exclusivamente por meio de uma única conexão com a Internet. A direção deseja melhorar a disponibilidade do ambiente. Analise por que contratar servidores redundantes no provedor de cloud pode não ser suficiente e proponha melhorias relacionadas à conectividade entre a empresa e a nuvem.
> Para garantir alta disponibilidade não deve garantir redundância somente no provedor de cloud, mas também na comunicação interna. Uma vez que a empresa possui apenas uma conexão com a internet, este se torna um ponto único de falha sem redundância, que em caso de falha, os serviços de cloud permanecem ativos, mas não podem ser acessados pela organização.
> Para solucionar o problema e aumentar a disponibilidade, a solução é contratar outros links de internet preferencialmente com operadoras distintas com roteadores redundantes. Em alguns cenários pode ser interessante um link dedicado entre a empresa e o provedor.

4. Um datacenter possui servidores com fontes redundantes, mas ambas as fontes estão conectadas ao mesmo circuito elétrico. Da mesma forma, dois links de rede utilizam o mesmo caminho físico de fibras até a operadora. Explique por que a simples duplicação de componentes não garante alta disponibilidade. Relacione sua resposta ao conceito de eliminação de pontos únicos de falha.
> A simples duplicação de componentes não garante alta disponibilidade quando os componentes redundantes compartilham a mesma dependência. No caso das fontes, ambas estão conectadas ao mesmo circuito elétrico; portanto, uma falha nesse circuito pode derrubar as duas simultaneamente. Da mesma forma, dois links de rede que utilizam o mesmo caminho físico de fibras continuam sujeitos ao mesmo ponto de falha, como o rompimento de um duto ou cabo.
> Assim, para eliminar pontos únicos de falha, a redundância deve ocorrer também nas dependências: circuitos elétricos independentes, caminhos físicos distintos e, quando possível, operadoras diferentes. O objetivo não é apenas duplicar componentes, mas garantir que uma única falha não consiga interromper todo o serviço.

6. Uma empresa pretende construir um pequeno datacenter para hospedar serviços críticos. Ela precisa definir conectividade, gerenciamento remoto, organização física e mecanismos de redundância. Proponha uma arquitetura conceitual para esse ambiente e justifique como pelo menos quatro elementos — por exemplo, múltiplos links, caminhos de cabeamento, alimentação elétrica, KVM/RSA/HMC, refrigeração ou monitoramento — contribuem para disponibilidade e operação do datacenter.
> Alguns dos pontos essenciais para um datacenter de qualquer porte:
> - **Redundância dos serviços com múltiplos provedores**, seja em internet, energia, backups etc;
> - Controle de acesso com biometrica e cartão de acesso, garantindo autenticação e autorização 
> - Escolha correta de cabos e sua organização, garantindo entrega de velocidade e posicionamento sem obstrução de vias de refrigeração e facilitando a manutenção;
> - Sistemas de automação e monitoramento do ambiente;
> - Sistema de resfriamento eficiênte e sustentavel, reduzindo consumo de água;

7. Um servidor físico possui capacidade suficiente para executar quatro sistemas diferentes. Em vez de instalar todos os aplicativos no mesmo sistema operacional, a empresa decide criar quatro máquinas virtuais. Explique qual papel o hypervisor desempenha nesse cenário e qual vantagem de isolamento é obtida em relação à execução de todas as aplicações diretamente no mesmo sistema operacional.
> O papel do hypervisor é criar uma abstração entre o hardware e SOs virtuais, permitindo que múltiplos SOs usem o mesmo hardware físico de forma gerenciavel. A principal vantagem de seu uso em relação a execução no mesmo sistema operacional é o isolamento, uma vez que seus pacotes e bibliotecas podem ser concorrentes em relação as demais aplicações, garantir a segurança da aplicação e garantia de replicação em diferentes ambientes.

8. Um aluno afirma que “uma VM é basicamente um container mais pesado”. Analise essa afirmação. Explique a principal diferença arquitetural entre os dois modelos considerando o papel do sistema operacional e do kernel.
> A principal diferença entre uma VM e um container é que a VM instância um SO próprio, enquanto o container compartilha o kernel da máquina host, consequentemente consumindo menos recursos.

9.  Uma empresa pretende utilizar VirtualBox em notebooks para treinamento e ESXi em servidores de produção. Explique por que essa escolha faz sentido considerando as diferenças entre hypervisors tipo 1 e tipo 2, sem limitar sua resposta apenas à facilidade de instalação.
> Hypervisors tipo 1 possuem maior complexidade na instalação e gestão do SO, uma vez que são menos flexíveis e mais caros, tendo seus casos de uso especializados em ambientes produtivos. Diferente de hypervisors tipo 2 que são feitos para executar dentro de SOs convencionais, reduzindo a performance mas facilitando o uso.

10. Durante uma manutenção programada, uma empresa precisa desligar um servidor físico sem interromper a máquina virtual que nele está executando. Explique qual recurso de virtualização pode ser utilizado e diferencie esse mecanismo de uma solução de High Availability, que atua diante da falha inesperada de um host.
> Para realizar tal migração os recursos que podem ser usados é uma combinação de snapshot para garantir recuperação do estado atual, da mesma forma a implementação de vMotion, que migra VMs entre diferentes hosts físicos. Diferente o HA, o vMotion é feito de forma planejada com o mínimo de indisponibilidade, enquanto o HA é feito para recuperação de falhas.

11. Uma empresa possui três hosts físicos formando um ambiente virtualizado. Em determinado momento:

    - um host apresenta utilização de CPU muito elevada;
    - outro possui grande quantidade de capacidade ociosa;
    - uma VM crítica não pode sofrer interrupção;
    - e existe risco de falha física de um dos servidores.

    Explique como conceitos como vMotion, DRS, High Availability e Fault Tolerance poderiam atuar nesse ambiente. Mostre claramente que esses mecanismos resolvem problemas diferentes e não são simplesmente quatro formas de fazer a mesma coisa.
> Os conceitos são semelhantes mas não fazem a mesma coisa:
> - vMotion: realizam migração entre hosts com VM em execução;
> - HA: realizam migração entre hosts após falha, reiniciando a VM em um novo host;
> - DRS: decide onde as VMs devem ficar para equilibrar recursos;
> - FT: Proporciona redundância completa em VMs críticas, mantendo uma réplica em execução simultânea em outro host.

12. Dois containers estão executando no mesmo host Linux. Um processo dentro do Container A consulta os processos em execução e não consegue visualizar normalmente os processos pertencentes ao Container B. Explique qual mecanismo do Linux contribui para esse isolamento e por que isso não significa que cada container possua seu próprio kernel.
> O mecanismo utilizado é o namespaces do Linux, que cria um ambiente isolado dentro do kernel, impedindo que diferentes namespaces acessem o mesmo conteúdo isolado, como PID, filesystem, rede etc.

13. Um servidor executa dois containers de processamento intensivo. O administrador deseja garantir que o Container A nunca utilize mais de 50% de uma CPU. Em outro cenário, ele deseja apenas que o Container B receba prioridade maior que o Container C quando ambos disputarem CPU. Explique por que `cpu.max` e `cpu.weight` atendem a objetivos diferentes.
> `cpu.max` define o tempo proporcional que um grupo de processos pode executar na CPU, por exemplo rodar 500 em 1000 microsegundos, o equivalente a executar 500µs a cada período de 1000 µs, o equivalente a 50% da CPU. Por outro lado, `cpu.weight` define a prioridade relativa a concorrência da CPU, por exemplo se o GrupoA tem 1024, e o GrupoB 256, por proporção, o GrupoA tende a receber cerca de 4x mais tempo de CPU que o GrupoB enquanto ambos estiverem disputando o processador.

14. Um administrador utiliza `cpuset.cpus` para permitir que determinado grupo execute apenas nas CPUs 0 e 1. Ele conclui que essas duas CPUs ficaram reservadas exclusivamente para esse grupo. Analise o raciocínio e explique por que CPU pinning não implica necessariamente exclusividade.
> O raciocinio está errado, uma vez que CPU Pinning não implica em exclusividade, apenas indica que o processo não pode sair do range de processadores especificado. Para garantir exclusividade é necessário que remova o processador do escalonador durante a etapa de boot.

15. Uma aplicação funciona corretamente no computador do desenvolvedor, mas falha quando instalada manualmente no ambiente de produção devido a diferenças de bibliotecas e dependências. Explique de que maneira o uso de imagem de container e Dockerfile pode reduzir esse tipo de problema e por que a imagem não deve ser confundida com o container em execução.
> O uso de containers reduz diferenças entre ambientes porque a aplicação é empacotada em uma imagem junto com suas dependências, bibliotecas e configurações necessárias. O Dockerfile define de forma reproduzível como essa imagem deve ser construída, evitando instalações manuais diferentes entre máquinas.
> Além disso, o container executa de forma isolada em relação ao sistema hospedeiro, diminuindo conflitos entre versões de bibliotecas e pacotes.
> A imagem não deve ser confundida com o container: a imagem é um modelo imutável que contém os arquivos e configurações necessários para a aplicação, enquanto o container é uma instância em execução dessa imagem.

16. Um servidor executa três aplicações conteinerizadas:

    - Aplicação A possui alto consumo de CPU;
    - Aplicação B realiza grande quantidade de operações de disco;
    - Aplicação C não pode ser afetada pelo comportamento das demais.

    Explique como namespaces e cgroups v2 atuariam em conjunto para isolar essas aplicações. Na resposta, diferencie explicitamente isolamento de visão do ambiente de controle de consumo de recursos e indique quais mecanismos poderiam ser aplicados a CPU e I/O.
> Namespaces isolam a visão do ambiente entre aplicações, de forma que cada container tenha sua própria visao sobre PID, network, filesystem, etc. Já o cgroups define o quanto de recurso computacional cada container pode utilizar.
> Para a Aplicação A, a solução é usar limitador de CPU como `cpu.max` ou `cpu.weight`. Para a Aplicação B limitador de I/O como `io.max` e `io.weight`. Para a Aplicação C o uso de namespaces para isolamento de visão acompanhado pela boa configuração de cgroups dos demais containeres.

17. Um Deployment declara três réplicas de uma aplicação. Um dos Pods é encerrado inesperadamente e, algum tempo depois, outro Pod é criado automaticamente. Explique por que isso acontece utilizando os conceitos de estado desejado, estado atual e reconciliação.
> O Kubernetes possui controladores que executam continuamente um processo de reconciliação, comparando o estado atual do cluster com o estado desejado declarado no Deployment. Ao detectar que existem apenas dois Pods quando deveriam existir três, o controlador solicita a criação de um novo Pod para restabelecer o estado desejado.

18. Explique por que normalmente não é recomendável tratar um Pod como se fosse um servidor permanente. Mostre como Deployment e ReplicaSet modificam a maneira como devemos pensar a disponibilidade das aplicações no Kubernetes.
> 

19. Um novo Pod precisa ser criado no cluster. Explique, em termos conceituais, o papel do API Server, Scheduler e kubelet desde a declaração desse recurso até sua execução em um Worker Node. Não é necessário descrever comandos.

20. Uma aplicação possui três Pods que podem ser destruídos e recriados, recebendo novos endereços IP. Ainda assim, os clientes internos precisam acessar a aplicação por um endereço estável. Explique qual problema o objeto Service resolve e por que acessar diretamente o IP de um Pod seria uma solução inadequada.
> 

21. Uma aplicação web em Kubernetes possui múltiplas réplicas e precisa:

    - manter três instâncias em funcionamento;
    - substituir automaticamente instâncias que falharem;
    - receber tráfego por um ponto lógico estável;
    - armazenar determinadas configurações fora da imagem;
    - armazenar credenciais de forma distinta das configurações comuns;
    - e preservar dados mesmo quando Pods forem recriados.

    Identifique os principais objetos Kubernetes que participariam dessa solução e explique a função de cada um. Sua resposta deve mostrar como Deployment/ReplicaSet, Service, ConfigMap, Secret e mecanismos de persistência se complementam.

22. Duas máquinas virtuais estão conectadas a uma rede lógica que existe sobre a mesma infraestrutura física utilizada por várias outras redes. Explique por que essa rede pode ser chamada de rede virtual mesmo continuando dependente de switches, cabos e interfaces físicas.

23. Um administrador precisa criar conectividade entre duas redes. Em uma rede tradicional, ele configuraria manualmente diversos switches e roteadores. Em um ambiente SDN, ele informa ao controlador a conectividade desejada. Explique o que muda na forma de administrar a rede e o que não muda no encaminhamento efetivo dos pacotes.

24. Explique a relação entre Application Plane, Control Plane e Data Plane em SDN utilizando o seguinte exemplo: uma aplicação solicita que a rede `10.1.0.0/16` possa comunicar-se com a rede `10.2.0.0/16`. Mostre como a intenção percorre as três camadas até resultar em encaminhamento de tráfego.

25. Um aluno afirma que “como SDN centraliza o controle da rede, todos os pacotes precisam passar pelo controlador SDN”. Analise a afirmação e explique a diferença entre controle logicamente centralizado e encaminhamento distribuído.

26. Um grande datacenter utiliza centenas de servidores com intenso tráfego entre aplicações internas. Compare conceitualmente uma arquitetura de rede hierárquica tradicional com uma Fabric Leaf-Spine. Explique por que múltiplos caminhos, previsibilidade e facilidade de automação tornam uma Fabric adequada a ambientes cloud e discuta como SDN pode complementar essa arquitetura sem substituir necessariamente os switches físicos.

27. Um roteador recebe duas rotas BGP para o mesmo prefixo. A primeira atravessa menos Autonomous Systems, mas a segunda foi configurada com uma política de preferência maior pela organização. Explique por que não se pode afirmar que o BGP sempre escolherá automaticamente o caminho com menor AS_PATH.

28. Um roteador BGP recebe uma rota cujo atributo NEXT_HOP aponta para um endereço IP que não está diretamente conectado a ele. Explique por que essa rota ainda pode ser utilizada e qual processo o roteador precisa realizar para descobrir como alcançar esse próximo salto.

29. Uma rede possui muitos roteadores participando de iBGP. Explique por que a exigência tradicional de Full Mesh se torna um problema à medida que a rede cresce e como um Route Reflector reduz a quantidade de sessões necessárias. Deixe claro que o Route Reflector não precisa necessariamente encaminhar o tráfego de dados entre os clientes.

30. Uma empresa possui uma Fabric IP funcionando corretamente entre seus switches Leaf e Spine. Mesmo assim, deseja que servidores conectados a diferentes Leafs possam participar da mesma rede lógica Layer 2. Explique por que apenas o Underlay IP não resolve esse requisito e como VXLAN, VTEP e VNI permitem criar essa rede lógica sobre a infraestrutura física.

31. Considere dois servidores pertencentes ao mesmo VNI, conectados a Leafs diferentes em uma Fabric VXLAN/EVPN. Explique, passo a passo e conceitualmente, como Underlay, VXLAN, VTEPs, MP-BGP e EVPN trabalham juntos para permitir a comunicação entre eles.

    Em sua resposta:

    - explique como o Underlay permite que os VTEPs se alcancem;
    - mostre a função do VXLAN no transporte do quadro;
    - explique como o VNI identifica a rede lógica;
    - explique como o EVPN distribui informações de MAC/IP;
    - e justifique por que essa abordagem reduz a dependência de Flood and Learn.
