# INATEL-C213-PID
Trabalho de Sistemas Embarcado - Controle Clássico

## Alunas
- Laura Ellen de Souza Santos - GEC 1657
- Letícia Moreira Mendes - GEC 1705
- Livia Jacklinne Ramos Moreira - GEC 1731

### Questão 1
Carregamos o arquivo TransferFunction, de acordo com número do nosso grupo e plotamos o gráfico

### Questão 2 
Fizemos a analise do gráfico e calculamos os valores de K, θ e τ, usando o metodo de SMITH
> K = 2,98

> θ = 4,925

> τ = 11,925

### Questão 3
Comparação da função Original com a Estimada. 
Conclusão: A função estimada teve seu atraso de propagação e seu intervalo, menor do que a função originada. Portanto a função estimada, atingiu a estabilidade mais rápido. 

### Questão 4
Erro em malha aberta:​ 2 - 5,97 =  -3,97
O erro em malha aberta representa a diferença entre o valor desejado (setpoint) e o valor real do sistema quando o controlador não está atuando. Então significa que o sistema quando não controlado está 3,97 abaixo do valor desejado.
 
Erro em malha fechada:​ 2 – 1,52 = 0,48
O erro em malha fechada representa a diferença entre o valor desejado (setpoint) e o valor real do sistema quando o controlador está atuando para manter o sistema próximo ao valor desejado. Então significa que quando o controlador está atuando, o sistema está apenas 0,48 unidades abaixo do valor desejado.


### Questão 5
O método CHR foi proposto em 1952, por Chien, Hrones e Reswick, que aborda a síntese completa de controladores para sistemas de tempo contínuo. Já o método que foi proposto por Cohen e Coon em 1953, tem um histórico de uso em sistemas industriais de controle de processos.​

Devido a ter mais flexibilidade, o CHR atende uma gama mais ampla de requisitos de desempenho, enquanto Cohen-Coon é utilizado para sintonizar controladores PID para atender a  desempenhos mais básicos e não é ideal quando é necessário desempenho de alta precisão.​

O CHR é mais complexo pois num primeiro momento tem-se o projeto da função de transferência em malha aberta, e depois o projeto o controlador. Enquanto que Cohen-Coon envolve uma abordagem mais direta para calcular os parâmetros do PID.​

Pela complexidade, pode ser mais dificil implementar o CHR manualmente, e por isso é frequentemente auxiliado por software de simulação e análise.​

### Questão 6
Foi realizado o ajuste fino no valor de Kp do método novo. Pois estava com o sobre sinal alto, e com isso o sistema pode ter que se adaptar para suportar esse sinal. Então o ideal é realizar esses ajustes para que isso não aconteça.

### Questão 7
Não identificamos nenhuma desvantagem no método clássico CRH1. O CHR1 visa minimizar ou eliminar o sobrevalor em um sistema de controle. O sobrevalor ocorre quando a resposta de um sistema ultrapassa temporariamente o valor de referência (setpoint) antes de convergir para o valor desejado e isso geralmente está associado a oscilações indesejadas.​
Então o sobrevalor que havia ao utilizar o método novo foi ajustado quando foi utilizado o método clássico.
