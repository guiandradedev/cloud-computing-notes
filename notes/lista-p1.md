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
>

16.   Uma empresa migrou uma máquina virtual de seu datacenter para um serviço IaaS e passou a acreditar que não precisa mais atualizar o sistema operacional porque “agora o servidor está na nuvem”. Explique o erro dessa interpretação utilizando o conceito de responsabilidade compartilhada.

17.   Compare IaaS, PaaS e SaaS do ponto de vista da responsabilidade do cliente. À medida que se passa de IaaS para PaaS e depois para SaaS, o que tende a acontecer com o controle e com a responsabilidade operacional do cliente? Explique utilizando exemplos de componentes da solução.

18.   Uma aplicação executada em PaaS sofreu uma invasão porque o desenvolvedor criou uma API sem autenticação adequada. O cliente afirma que o provedor deveria assumir a responsabilidade porque a aplicação estava hospedada na infraestrutura dele. Analise essa afirmação utilizando o modelo de responsabilidade compartilhada.

19. **Estudo de caso:** Uma empresa utiliza um sistema financeiro SaaS. O fornecedor mantém o software atualizado, realiza backups da plataforma e protege sua infraestrutura. Um funcionário da empresa cliente recebe privilégios administrativos excessivos e exporta informações financeiras confidenciais.
Analise o incidente e explique:
    - quais controles estavam sob responsabilidade do provedor;
    - quais estavam sob responsabilidade do cliente;
    - por que utilizar SaaS não transfere toda a responsabilidade de segurança ao provedor.

20. **Estudo de caso:** Uma empresa possui a seguinte arquitetura:
    - máquinas virtuais em IaaS executando sistemas legados;
    - uma nova aplicação desenvolvida em PaaS;
    - e-mail corporativo fornecido como SaaS.

    Após uma auditoria foram encontrados três problemas:

    1. o sistema operacional de uma VM não recebe patches há seis meses;
    2. a aplicação PaaS possui permissões excessivas no acesso ao banco de dados;
    3. uma conta administrativa do serviço de e-mail utiliza senha fraca e não possui controles adicionais de acesso.

    Para cada problema, identifique quem possui a responsabilidade principal — cliente ou provedor — e explique por que a divisão de responsabilidades muda entre os três casos. Ao final, explique por que a frase “quanto mais gerenciado é o serviço, menos responsabilidade o cliente possui” pode ser útil, mas também perigosa se interpretada de forma absoluta.
> [...]

21.  Duas empresas utilizam a mesma quantidade de máquinas virtuais em cloud. A empresa A cria e administra os recursos manualmente, sem políticas comuns. A empresa B possui processos padronizados, governança e monitoramento do ambiente. Explique por que a quantidade de recursos em cloud não é suficiente para determinar a maturidade das duas organizações.

22.  Uma empresa possui diversos departamentos utilizando serviços de nuvem de forma independente. Alguns utilizam IaaS, outros SaaS e alguns criaram ambientes de desenvolvimento sem conhecimento da área central de TI. Explique quais características desse cenário indicam um estágio inicial de maturidade e quais mudanças seriam necessárias para que a organização avançasse para um uso mais repetível e coordenado.

23.  **Estudo de caso:** Uma empresa apresenta as seguintes características:

    - utiliza cloud em praticamente todos os seus sistemas;
    - possui políticas centralizadas de segurança e governança;
    - os processos de implantação são definidos e repetíveis;
    - existe monitoramento dos ambientes;
    - porém métricas de custo, desempenho e eficiência ainda não são utilizadas sistematicamente para otimização.

    Com base no CMM apresentado em aula, indique em que região da escala de maturidade essa organização se encontra e justifique sua análise. Em seguida, explique quais mudanças seriam esperadas para que ela avançasse para o próximo nível.

24. **Estudo de caso:** Uma grande organização realizou uma avaliação CMM e encontrou o seguinte cenário:

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
> Anotar sobre funções avançadas de virtualização que eu não vi

11. Uma empresa possui três hosts físicos formando um ambiente virtualizado. Em determinado momento:

    - um host apresenta utilização de CPU muito elevada;
    - outro possui grande quantidade de capacidade ociosa;
    - uma VM crítica não pode sofrer interrupção;
    - e existe risco de falha física de um dos servidores.

    Explique como conceitos como vMotion, DRS, High Availability e Fault Tolerance poderiam atuar nesse ambiente. Mostre claramente que esses mecanismos resolvem problemas diferentes e não são simplesmente quatro formas de fazer a mesma coisa.

12. Dois containers estão executando no mesmo host Linux. Um processo dentro do Container A consulta os processos em execução e não consegue visualizar normalmente os processos pertencentes ao Container B. Explique qual mecanismo do Linux contribui para esse isolamento e por que isso não significa que cada container possua seu próprio kernel.

13. Um servidor executa dois containers de processamento intensivo. O administrador deseja garantir que o Container A nunca utilize mais de 50% de uma CPU. Em outro cenário, ele deseja apenas que o Container B receba prioridade maior que o Container C quando ambos disputarem CPU. Explique por que `cpu.max` e `cpu.weight` atendem a objetivos diferentes.

14. Um administrador utiliza `cpuset.cpus` para permitir que determinado grupo execute apenas nas CPUs 0 e 1. Ele conclui que essas duas CPUs ficaram reservadas exclusivamente para esse grupo. Analise o raciocínio e explique por que CPU pinning não implica necessariamente exclusividade.

15. Uma aplicação funciona corretamente no computador do desenvolvedor, mas falha quando instalada manualmente no ambiente de produção devido a diferenças de bibliotecas e dependências. Explique de que maneira o uso de imagem de container e Dockerfile pode reduzir esse tipo de problema e por que a imagem não deve ser confundida com o container em execução.

16. Um servidor executa três aplicações conteinerizadas:

    - Aplicação A possui alto consumo de CPU;
    - Aplicação B realiza grande quantidade de operações de disco;
    - Aplicação C não pode ser afetada pelo comportamento das demais.

    Explique como namespaces e cgroups v2 atuariam em conjunto para isolar essas aplicações. Na resposta, diferencie explicitamente isolamento de visão do ambiente de controle de consumo de recursos e indique quais mecanismos poderiam ser aplicados a CPU e I/O.

17. Um Deployment declara três réplicas de uma aplicação. Um dos Pods é encerrado inesperadamente e, algum tempo depois, outro Pod é criado automaticamente. Explique por que isso acontece utilizando os conceitos de estado desejado, estado atual e reconciliação.

18. Explique por que normalmente não é recomendável tratar um Pod como se fosse um servidor permanente. Mostre como Deployment e ReplicaSet modificam a maneira como devemos pensar a disponibilidade das aplicações no Kubernetes.

19. Um novo Pod precisa ser criado no cluster. Explique, em termos conceituais, o papel do API Server, Scheduler e kubelet desde a declaração desse recurso até sua execução em um Worker Node. Não é necessário descrever comandos.

20. Uma aplicação possui três Pods que podem ser destruídos e recriados, recebendo novos endereços IP. Ainda assim, os clientes internos precisam acessar a aplicação por um endereço estável. Explique qual problema o objeto Service resolve e por que acessar diretamente o IP de um Pod seria uma solução inadequada.

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
