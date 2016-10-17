aioclon <- nuevoaio
soloclon <- nuevosolo
atipicosT <- c()
atipicosT2 <- c()

#aioclon$Total <- aioclon$Total+aioclon$Celery
#soloclon$Total <- soloclon$Total+soloclon$Celery

quitaratipicos <- function(valor){
  atipicos3 <- c()
  for(i in c(1:length(aioclon$Total))){
    if(aioclon$Total[i] > valor)
    {atipicos3 <- c(atipicos3, i)}
  }
  print(length(atipicos3))
  atipicosT <<- c(atipicosT, atipicos3)
}
quitaratipicos2 <- function(valor){
  atipicos3 <- c()
  for(i in c(1:length(soloclon$Total))){
    if(soloclon$Total[i] > valor)
    {atipicos3 <- c(atipicos3, i)}
  }
  print(length(atipicos3))
  atipicosT2 <<- c(atipicosT, atipicos3)
}

quitaratipicos(2)
quitaratipicos2(2)

aioclon <- aioclon[-atipicosT,]
aioclon$Procesos <- c(1:length(aioclon$Procesos))
soloclon <- soloclon[-atipicosT2,]
soloclon$Procesos <- c(1:length(soloclon$Procesos))

plot(aioclon$Procesos,aioclon$Total, xlab = "Procesos", ylab = "Tiempo (ms)", col="black", pch = 20, cex=0.1)
abline(lm(aioclon$Total~aioclon$Procesos), col="red")
par(new = TRUE)
plot(soloclon$Procesos,soloclon$Total, xlab="", ylab = "", axes = FALSE,col="gray", pch = 20, cex=0.1)
abline(lm(soloclon$Total~soloclon$Procesos), col="darkred")
title(main = "Tiempo de procesamiento total en Raspberry y servidor \n para ambos escenarios")
legend("topleft",legend = c("Escenario 1","Escenario 2"), pt.bg = c("black","gray"),pch = 22)
