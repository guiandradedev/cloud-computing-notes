# Resumo geral — Computação em Nuvem

Este documento reúne os pontos mais importantes do `README.md` da disciplina e complementa a parte de redes avançadas da aula-13 com os conteúdos de BGP, VXLAN e EVPN que ainda não estavam integrados.

## 1. O que é computação em nuvem

Computação em nuvem é um modelo no qual recursos de TI — como processamento, armazenamento, redes e aplicações — são disponibilizados sob demanda, normalmente pela Internet, com provisionamento rápido, gerenciamento reduzido e cobrança baseada no uso.

As definições apresentadas convergem para algumas ideias centrais:

- acesso conveniente e sob demanda a um pool compartilhado de recursos;
- provisionamento e liberação rápidos;
- elasticidade e escalabilidade;
- acesso por interfaces de autoatendimento e APIs;
- pagamento proporcional ao consumo;
- menor necessidade de investimento inicial em infraestrutura própria.

A nuvem não é apenas um conjunto de servidores remotos. Para ser considerada cloud, a infraestrutura deve oferecer características como automação, provisionamento sob demanda, medição de consumo, elasticidade, gerenciamento centralizado e abstração dos recursos físicos.

## 2. Características, benefícios e desafios

### Características principais

- **Elasticidade:** ajuste automático dos recursos conforme a demanda, inclusive aumentando e reduzindo a capacidade dentro de limites predefinidos.
- **Escalabilidade:** capacidade de ampliar ou reduzir recursos para suportar mudanças de carga. Pode ocorrer de forma planejada ou automática.
- **Flexibilidade:** adaptação da infraestrutura a diferentes necessidades, como trocar o tipo de VM, alterar configurações de rede, mudar o mecanismo de banco de dados ou ligar e desligar recursos remotamente.
- **Uso sob demanda:** o consumidor provisiona recursos quando precisa, sem depender de intervenção manual do provedor.
- **Acesso ubíquo:** os serviços podem ser acessados de diferentes locais, respeitando as limitações e políticas de segurança da rede.
- **Pooling de recursos:** o provedor agrupa recursos físicos e os distribui dinamicamente entre vários consumidores.
- **Multitenancy:** vários consumidores compartilham a infraestrutura com isolamento de dados, configurações, desempenho e permissões.
- **Medição e pagamento por uso:** o consumo é monitorado para cobrança e otimização.
- **Resiliência:** capacidade de continuar funcionando ou se recuperar rapidamente diante de falhas.

### Benefícios

A cloud reduz o investimento inicial, diminui a ociosidade, acelera a implantação de soluções e permite ajustar a capacidade ao consumo real. Também facilita testes, expansão de aplicações, automação, recuperação de desastres e acesso a tecnologias que seriam caras para manter localmente.

### Desafios

- **Segurança e privacidade:** a organização perde parte do controle físico e precisa proteger dados, identidades, aplicações e configurações.
- **Responsabilidade compartilhada:** o provedor protege a infraestrutura que administra, mas o consumidor continua responsável por aquilo que configura e utiliza.
- **Dependência do fornecedor:** serviços proprietários podem causar lock-in e dificultar a migração para outro provedor.
- **Complexidade operacional:** cloud exige novas ferramentas, conhecimentos, automação, monitoramento e governança.
- **Investigação e logs:** o consumidor pode não ter acesso direto a todos os equipamentos e registros necessários para uma perícia.
- **Conformidade:** a localização dos dados e a legislação aplicável podem não ser óbvias, especialmente em ambientes internacionais.
- **Custos:** o pagamento por uso é vantajoso, mas configurações inadequadas e recursos ociosos podem gerar gastos elevados.

## 3. Raízes tecnológicas da cloud

### Clustering

Cluster é um conjunto de recursos independentes e interconectados que atua como um único sistema. É normalmente mais homogêneo, localizado e baseado em comunicação rápida, oferecendo alta disponibilidade, failover e distribuição de carga.

- **Horizontal:** adiciona nós ao cluster. Favorece escalabilidade, distribuição de carga e resiliência.
- **Vertical:** aumenta CPU, memória ou outros recursos dos nós existentes. Pode ser útil quando a aplicação depende de um único nó de alto desempenho.

### Grid Computing

Grid organiza recursos heterogêneos e distribuídos geograficamente em pools lógicos, formando um supercomputador virtual. Diferentemente do cluster, não exige hardware homogêneo nem localização única; utiliza middleware para coordenar os recursos.

### Virtualização

Virtualização cria instâncias lógicas de recursos físicos. Ela permite que vários usuários, sistemas operacionais ou aplicações compartilhem o mesmo hardware com isolamento, flexibilidade e melhor aproveitamento.

Essas tecnologias ajudaram a viabilizar a cloud, mas não são suficientes isoladamente. Um ambiente com VMs ou clusters só se torna cloud quando também oferece automação, provisionamento sob demanda, medição, elasticidade e gerenciamento de serviços.

## 4. Funções, papéis e modelos de serviço

### Papéis no ecossistema

- **Provedor:** oferece e administra a infraestrutura e os serviços.
- **Consumidor:** utiliza e gerencia os recursos contratados.
- **Proprietário:** possui legalmente o serviço, o software ou os dados.
- **Administrador de recursos:** gerencia disponibilidade, desempenho, segurança e alocação.
- **Auditor:** avalia de forma independente segurança, privacidade e desempenho.
- **Broker:** intermedeia a contratação e o gerenciamento entre consumidores e provedores.
- **Carrier:** fornece a conectividade de rede para acesso aos serviços.

Também é importante distinguir:

- **Limite organizacional:** fronteira física dos recursos que a organização controla diretamente;
- **Limite de confiança:** fronteira lógica que inclui componentes de terceiros nos quais a organização decidiu confiar.

### IaaS, PaaS e SaaS

| Modelo | O provedor administra | O consumidor administra | Característica |
|---|---|---|---|
| **IaaS** | Hardware, rede física, storage, virtualização e disponibilidade da infraestrutura | SO, patches, aplicações, dados, firewall e configurações | Mais controle e mais responsabilidade |
| **PaaS** | Infraestrutura, SO, middleware, runtime e ferramentas da plataforma | Código, dados, configurações e permissões da aplicação | Foco no desenvolvimento |
| **SaaS** | Aplicação completa, plataforma e infraestrutura | Usuários, configurações, dados inseridos e uso adequado | Mais simples, porém menos flexível |

A responsabilidade do cliente nunca desaparece completamente. Mesmo em SaaS, ele precisa controlar acessos, proteger dados, configurar o serviço e cumprir suas obrigações de conformidade.

## 5. Modelos de implantação e serviços relacionados

- **Nuvem pública:** infraestrutura de um provedor, compartilhada entre consumidores. Oferece escala e menor investimento, mas reduz o controle direto.
- **Nuvem privada:** ambiente dedicado a uma organização. Proporciona maior controle e personalização, com custo e responsabilidade maiores.
- **Nuvem comunitária:** ambiente compartilhado por organizações com requisitos comuns, como saúde, finanças ou projetos colaborativos.
- **Nuvem híbrida:** integração entre nuvens públicas, privadas e/ou comunitárias. Oferece flexibilidade, mas exige conectividade, identidade, segurança e gerenciamento integrados.
- **Multicloud:** uso de mais de um provedor de nuvem; não é necessariamente híbrida, pois pode envolver somente nuvens públicas.
- **Edge Computing:** aproxima processamento e armazenamento dos usuários ou dispositivos, reduzindo latência.
- **Serverless:** o provedor administra a infraestrutura de execução; o consumidor concentra-se no código acionado por eventos, APIs ou agendamentos.
- **Nuvem soberana:** considera onde os dados estão armazenados, quais leis se aplicam e quem pode acessá-los.

Ter um datacenter próprio não significa automaticamente possuir uma nuvem privada. É necessário oferecer automação, autoatendimento, elasticidade, medição e gerenciamento adequado.

## 6. Cloud Maturity Model (CMM)

O modelo de maturidade avalia a evolução da organização em diferentes domínios, como tecnologia, segurança, finanças, pessoas e processos. A avaliação não deve ser reduzida a uma nota única: uma organização pode estar avançada em tecnologia e atrasada em FinOps, capacitação ou governança.

Os níveis apresentados são:

0. **Legacy:** processos tradicionais, pouca automação e forte dependência de infraestrutura antiga;
1. **Initial/Ad-hoc:** iniciativas isoladas e pouco padronizadas;
2. **Repeatable/Opportunistic:** práticas repetíveis, mas ainda inconsistentes entre equipes;
3. **Defined/Systematic:** processos definidos, padronizados e aplicados de forma organizada;
4. **Measured/Measurable:** uso de métricas, indicadores e acompanhamento de resultados;
5. **Optimized:** melhoria contínua, automação e otimização orientada por dados.

O CMM serve para avaliar o estado atual, definir o estado desejado, identificar gaps, construir um roadmap e acompanhar a evolução.

## 7. Redes, conectividade e datacenters

A rede é parte essencial da experiência em cloud. CPU e memória mais rápidas não resolvem necessariamente uma aplicação lenta se houver latência elevada, distância geográfica, jitter, perda de pacotes, baixa largura de banda ou muitas chamadas entre serviços.

- **Latência:** tempo para um pacote chegar ao destino.
- **Largura de banda:** volume máximo de dados que pode ser transmitido.
- **Jitter:** variação da latência.
- **Perda de pacotes:** dados enviados que não chegam ao destino.

> Largura de banda é a capacidade do caminho; latência é o tempo de percurso. Uma conexão pode ter muita largura de banda e ainda apresentar latência, jitter ou perdas inadequadas para aplicações em tempo real.

A Internet é formada por redes interconectadas. Provedores Tier 1 fazem a interconexão global; Tier 2 atuam regionalmente; Tier 3 conectam usuários finais. Peering, trânsito, múltiplos ISPs, links dedicados, MPLS e VPNs influenciam desempenho, segurança, custo e disponibilidade.

### Infraestrutura de datacenter

Um datacenter combina:

- camada física de servidores, racks, energia e refrigeração;
- camada virtualizada para abstração de recursos;
- plataformas de gerenciamento, automação e monitoramento;
- redundância de energia, rede, storage e serviços.

KVM, RSA e HMC permitem gerenciamento remoto e diagnóstico de servidores. Cabeamento estruturado, caminhos físicos independentes, fibra para maiores distâncias e organização dos cabos contribuem para desempenho e manutenção.

UPS mantém os equipamentos durante interrupções curtas; geradores fornecem energia em falhas prolongadas. Redundância só é efetiva se eliminar dependências compartilhadas: duas fontes no mesmo circuito ou dois links no mesmo duto continuam sujeitos ao mesmo ponto único de falha.

## 8. Virtualização de servidores, redes e storage

O **hypervisor** cria uma camada entre o hardware e os sistemas operacionais convidados, distribuindo CPU, memória, armazenamento e dispositivos para múltiplas VMs.

- **Hypervisor tipo 1:** executa diretamente sobre o hardware, sendo comum em produção.
- **Hypervisor tipo 2:** executa sobre um SO convencional, sendo conveniente para notebooks, laboratórios e treinamento.
- **VM:** possui seu próprio sistema operacional e kernel, oferecendo forte isolamento, mas com maior consumo de recursos.
- **Imagem/template:** modelo usado para criar VMs de maneira consistente.
- **Clone:** cópia de uma VM; identificadores como MAC address precisam ser tratados para evitar conflitos.

Recursos avançados incluem:

- **vMotion:** migração planejada de uma VM em execução entre hosts;
- **DRS:** decisão e balanceamento da localização das VMs;
- **High Availability:** reinício ou recuperação de VMs após falha de um host;
- **Fault Tolerance:** manutenção de uma réplica ativa para workloads críticos;
- **Snapshots e clones:** preservação de estados e criação de cópias, sem substituir uma estratégia completa de backup.

Na virtualização de rede aparecem vSwitches, roteadores e firewalls virtuais, hypervisors de rede, controladores e redes Overlay. Na virtualização de storage aparecem SAN, NAS, pools, snapshots e abstrações de armazenamento.

### RAID

- **RAID 0:** distribuição dos dados entre discos, aumentando capacidade e desempenho, mas sem redundância.
- **RAID 1:** espelhamento; aumenta proteção, mas reduz a capacidade útil.
- **RAID 5:** usa striping e paridade distribuída, permitindo recuperar a falha de um disco.

RAID melhora disponibilidade do storage, mas não substitui backup nem proteção contra falhas do servidor, do datacenter ou de exclusão acidental.

## 9. Multitenancy e containers

Multitenancy permite que vários consumidores compartilhem recursos com isolamento lógico. O provedor precisa controlar identidade, permissões, desempenho, armazenamento, rate limiting, monitoramento e políticas de penalização para evitar que um tenant prejudique os demais.

### Containers versus VMs

Uma VM virtualiza um sistema completo e executa seu próprio kernel. Um container isola processos, arquivos, rede e recursos, mas compartilha o kernel do host. Por isso, containers são mais leves e rápidos, porém não equivalem a VMs em arquitetura ou isolamento.

### Namespaces e cgroups

- **Namespaces:** isolam a visão do processo sobre PID, rede, filesystem, usuários e outros recursos.
- **cgroups v2:** controlam quanto recurso um grupo de processos pode consumir.

Exemplos de controle:

- `cpu.max`: limita o consumo absoluto, como 500 microssegundos a cada período de 1000, equivalente a 50% de uma CPU;
- `cpu.weight`: define prioridade relativa quando grupos competem pela CPU;
- `cpuset.cpus`: restringe em quais CPUs o grupo pode executar, mas não garante exclusividade;
- `io.max` e `io.weight`: limitam ou priorizam operações de entrada e saída;
- limites de memória evitam que um container consuma todo o host.

CPU pinning define afinidade, mas não reserva automaticamente os processadores. Exclusividade requer retirar as CPUs do escalonamento geral, por exemplo com configurações apropriadas de boot.

### Docker

Uma **imagem** é um modelo imutável contendo a aplicação e suas dependências. Um **container** é uma instância executável dessa imagem. O `Dockerfile` torna a construção reproduzível; `docker commit` pode registrar um estado, mas Dockerfiles são preferíveis para rastreabilidade e automação.

## 10. Kubernetes

Kubernetes é uma plataforma de orquestração orientada a objetos e ao estado desejado. O usuário declara como o sistema deve estar; controladores comparam estado desejado e estado atual e executam reconciliação contínua.

### Componentes

- **Control Plane:** API Server, Scheduler, controladores e armazenamento do estado do cluster;
- **Worker Nodes:** executam os Pods e possuem kubelet, runtime de containers e componentes de rede;
- **API Server:** recebe e valida declarações de recursos;
- **Scheduler:** escolhe o Worker Node para cada Pod;
- **kubelet:** garante que os Pods atribuídos ao Node estejam executando.

### Objetos importantes

- **Pod:** unidade básica de execução, normalmente descartável;
- **Deployment:** declara a aplicação e o número desejado de réplicas;
- **ReplicaSet:** mantém a quantidade de Pods definida;
- **Service:** oferece um endereço lógico estável e distribui tráfego para Pods;
- **ConfigMap:** armazena configurações não sensíveis;
- **Secret:** armazena credenciais e dados sensíveis;
- **Volume/PV/PVC:** fornecem armazenamento persistente para aplicações;
- **Ingress:** expõe aplicações HTTP/HTTPS e encaminha para Services, exigindo um Ingress Controller;
- **Labels e Selectors:** associam objetos e definem quais Pods recebem tráfego.

Pods podem ser recriados e receber novos IPs; por isso, clientes devem acessar Services, não IPs diretamente. Scheduling e regras como anti-affinity podem distribuir réplicas entre Nodes ou zonas, reduzindo impacto de falhas.

## 11. Redes virtuais, SDN, NFV e Fabric

Redes virtuais são abstrações lógicas sobre equipamentos físicos. VLANs, VXLANs, VNets, VPCs, redes de VMs e redes de containers são exemplos.

### SDN

SDN separa a intenção e o controle da rede do encaminhamento de pacotes:

- **Application Plane:** declara necessidades e políticas;
- **Control Plane:** interpreta essas intenções e calcula/configura regras;
- **Data Plane:** encaminha pacotes usando as tabelas e regras instaladas.

O controle pode ser logicamente centralizado, mas os pacotes normalmente continuam sendo encaminhados de forma distribuída pelos switches e roteadores. SDN aumenta automação, visibilidade, padronização e velocidade de provisionamento sem eliminar necessariamente os equipamentos físicos.

### NFV

NFV transforma funções tradicionalmente executadas por appliances dedicados em software, como firewalls, roteadores, balanceadores e VPNs. Isso reduz dependência de hardware específico e permite implantação mais flexível, mas exige desempenho, segurança, orquestração e monitoramento adequados.

### Fabric Leaf-Spine

Uma Fabric fornece conectividade previsível e múltiplos caminhos. Na arquitetura Leaf-Spine, cada Leaf conecta-se a todos os Spines; os servidores conectam-se aos Leafs. O modelo é adequado ao tráfego **East-West**, comum entre aplicações internas de um datacenter.

Em um Underlay Layer 3, o ECMP distribui o tráfego por caminhos de mesmo custo e o Spanning Tree deixa de bloquear caminhos paralelos. SDN pode automatizar a configuração e as políticas da Fabric, enquanto os switches continuam encaminhando os dados.

## 12. Complemento da aula-13: BGP, VXLAN e EVPN

Esta é a parte que estava apenas parcialmente registrada no `README.md`.

### BGP

O **Border Gateway Protocol** troca informações de alcançabilidade entre redes e escolhe caminhos por políticas e atributos, não apenas pelo menor custo. Uma sessão BGP é estabelecida sobre TCP, normalmente na porta 179.

- **AS:** conjunto de redes sob uma política comum;
- **ASN:** identificador do AS;
- **eBGP:** sessão entre ASs diferentes;
- **iBGP:** sessão dentro do mesmo AS;
- **AS_PATH:** sequência de ASs atravessados, usada na seleção e na prevenção de loops;
- **NEXT_HOP:** próximo endereço IP usado para alcançar a rota;
- **LOCAL_PREF:** preferência de saída dentro do AS;
- **MED, Communities e Weight:** atributos adicionais para políticas.

O BGP é um protocolo **Path Vector**. Um roteador pode receber várias rotas para o mesmo prefixo e escolher a melhor conforme a política configurada; portanto, o menor AS_PATH não é necessariamente o critério dominante.

No iBGP tradicional, a Full Mesh cresce de forma complexa. Route Reflectors reduzem a quantidade de sessões ao refletir anúncios entre clientes, mas não precisam ser o caminho físico do tráfego de dados. Em Data Centers, é comum usar eBGP entre Leafs e Spines, atribuindo ASNs diferentes aos equipamentos.

### Underlay e Overlay

- **Underlay:** rede IP física que conecta os switches e fornece alcançabilidade entre os VTEPs.
- **Overlay:** rede lógica criada sobre o Underlay, podendo oferecer conectividade Layer 2 independentemente da topologia física.

A arquitetura Leaf-Spine usa múltiplos caminhos e ECMP no Underlay. O Overlay cria redes virtuais para workloads, tenants e aplicações.

### Limitações das VLANs

VLANs usam identificadores de 12 bits e oferecem aproximadamente 4.000 VLANs utilizáveis. Em ambientes grandes e multi-tenant, isso pode ser insuficiente. Além disso, estender grandes domínios Layer 2 amplia broadcast e prejudica a escalabilidade.

### VXLAN

**VXLAN (Virtual Extensible LAN)** transporta um quadro Ethernet dentro de um pacote UDP/IP. Dessa forma, uma rede Layer 2 lógica pode atravessar um núcleo Layer 3.

O processo é:

1. O Leaf de entrada identifica a rede local e o VNI correspondente.
2. O quadro Ethernet é encapsulado com VXLAN, UDP e IP.
3. O Underlay encaminha o pacote usando apenas os IPs externos.
4. O Leaf remoto remove os cabeçalhos externos e entrega o quadro original.

A porta UDP normalmente usada é a **4789**.

### VNI

O **VNI (VXLAN Network Identifier)** possui 24 bits e permite aproximadamente 16 milhões de redes lógicas. Uma VLAN local pode ser mapeada para um VNI para atravessar a Fabric. VNIs diferentes mantêm redes virtuais logicamente separadas sobre a mesma infraestrutura física.

### VTEP

O **VTEP (VXLAN Tunnel Endpoint)** encapsula e desencapsula pacotes VXLAN. Normalmente está nos switches Leaf, embora também possa existir em hypervisors ou dispositivos virtuais. Cada VTEP usa um endereço IP no Underlay; para a rede física, o tráfego VXLAN é apenas tráfego IP entre VTEPs.

### Flood and Learn

O VXLAN transporta os quadros, mas precisa de informações para descobrir em qual VTEP remoto está cada MAC. No modelo **Flood and Learn**, o VTEP aprende MACs observando o tráfego local; quando o destino é desconhecido, replica broadcast, unknown unicast ou multicast para os VTEPs participantes do VNI.

Esse modelo funciona, mas aumenta o tráfego e reduz a escalabilidade. Por isso, redes maiores utilizam um Control Plane para distribuir explicitamente as localizações.

### EVPN e MP-BGP

**EVPN (Ethernet VPN)** é o Control Plane que distribui informações Ethernet. Ele anuncia MAC addresses, IPs, VNIs e a localização dos endpoints através de **MP-BGP**.

O **MP-BGP** amplia o BGP para transportar diferentes tipos de NLRI, além de prefixos IPv4. Uma sessão continua sendo BGP sobre TCP, mas pode negociar várias **Address Families**, identificadas por AFI e SAFI, como:

- IPv4 Unicast;
- IPv6 Unicast;
- VPNv4/VPNv6;
- L2VPN EVPN.

No caso de VXLAN/EVPN, a família L2VPN EVPN permite anunciar MACs, IPs e a localização dos endpoints.

### EVPN Route Type 2

A **Route Type 2 — MAC/IP Advertisement** anuncia que um MAC, e opcionalmente seu IP associado, pode ser alcançado por determinado VTEP.

Exemplo:

1. Uma VM com MAC `AA:AA:AA:AA:AA:01` conecta-se ao Leaf 1 e pertence ao VNI `10010`.
2. O Leaf 1 aprende localmente esse MAC.
3. O Leaf 1 anuncia o MAC por BGP EVPN.
4. O Leaf 2 associa o MAC ao IP do VTEP do Leaf 1.
5. Quando precisar enviar tráfego, o Leaf 2 cria o túnel VXLAN diretamente para o Leaf 1.

### Fluxo completo VXLAN/EVPN

Quando dois servidores estão em Leafs diferentes, mas no mesmo VNI:

1. O EVPN informa ao Leaf de origem onde está o MAC/IP remoto.
2. O Leaf de origem identifica o VNI da rede lógica.
3. O VTEP encapsula o quadro Ethernet em VXLAN/UDP/IP.
4. Os Spines encaminham o pacote pelo Underlay IP, normalmente usando ECMP.
5. O VTEP remoto desencapsula o pacote.
6. O quadro Ethernet é entregue ao servidor de destino.

Assim, cada tecnologia possui uma função específica:

| Tecnologia | Papel |
|---|---|
| Leaf-Spine | Topologia física com múltiplos caminhos |
| Underlay IP | Conectividade entre switches e VTEPs |
| BGP/eBGP | Roteamento e políticas do Underlay |
| VXLAN | Transporte do quadro do Overlay |
| VNI | Identificação da rede lógica |
| VTEP | Encapsulamento e desencapsulamento |
| MP-BGP EVPN | Distribuição de MAC/IP/VNI |
| Route Type 2 | Anúncio de MAC e IP associado |

## 13. Síntese final

Computação em nuvem combina virtualização, automação, redes, armazenamento, segurança e modelos de serviço para oferecer recursos sob demanda, escaláveis e medidos. O consumidor deve compreender não apenas a tecnologia, mas também custos, governança, maturidade, segurança, responsabilidade compartilhada e dependência de fornecedores.

Nos datacenters, a infraestrutura física precisa fornecer energia, refrigeração, conectividade e redundância. Sobre ela, virtualização, containers, Kubernetes, SDN, NFV e Fabrics permitem abstrair, automatizar e distribuir recursos.

Na parte de redes avançadas, a arquitetura mais importante é:

```text
Leaf-Spine + Underlay IP/eBGP + VXLAN + MP-BGP EVPN
```

O **Underlay** conecta os VTEPs, o **BGP** escolhe caminhos e aplica políticas, o **VXLAN** transporta redes Layer 2 sobre IP e o **EVPN** anuncia onde estão os MACs e IPs. A combinação reduz flooding, aumenta a escala de segmentos virtuais e permite construir redes multi-tenant independentes da topologia física.

