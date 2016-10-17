atipicosT <- c()
aio.celery <- read.table("aio-celery.txt")
solo.celery2 <- data.frame("Proceso" = c(1:length(aio.celery$V1)), "Tiempo" = aio.celery$V1)
procesos <- c(1:3469)
quitaratipicos <- function(valor){
  atipicos <- c()
  for(i in procesos){
    if(solo.celery2$Tiempo[i] > valor)
      {atipicos <- c(atipicos, i)}
  }
  print(length(atipicos))
  atipicosT <<- c(atipicosT, atipicos)
}

aio.server <- read.table("aio-server.txt")

solo.server2 <- data.frame("Proceso" = c(1:length(aio.server$V1)), "Tiempo" = aio.server$V1)
procesos <- c(1:3469)

quitaratipicos2 <- function(valor){
  atipicos2 <- c()
  for(i in procesos){
    if(solo.server2$Tiempo[i] > valor)
      {atipicos2 <- c(atipicos2, i)}
  }
  print(length(atipicos2))
  atipicosT <<- c(atipicosT, atipicos2)
}

aio.rasp <- read.table("aio-rasp.txt")
solo.raspb2 <- data.frame("Proceso" = c(1:length(aio.rasp$V1)), "Tiempo" = aio.rasp$V1)
procesos <- c(1:3469)

quitaratipicos3 <- function(valor){
  atipicos3 <- c()
  for(i in procesos){
    if(solo.raspb2$Tiempo[i] > valor)
      {atipicos3 <- c(atipicos3, i)}
  }
  print(length(atipicos3))
  atipicosT <<- c(atipicosT, atipicos3)
}

quitaratipicos(0.04)
quitaratipicos2(0.003)
quitaratipicos3(0.002)
print(atipicosT)

fullaio <- data.frame("Procesos" = procesos, "Celery" = solo.celery2$Tiempo, "Servidor" = solo.server2$Tiempo, "Raspberry" = solo.raspb2$Tiempo)

atipicosT2 <- as.factor(atipicosT)
x <- levels(atipicosT2)

nuevoaio <- fullaio[-c(as.integer(x)),]
nuevoaio$Procesos <- c(1:length(nuevoaio$Procesos))

nuevoaio$Celery <- nuevoaio$Celery * 1000
nuevoaio$Servidor <- nuevoaio$Servidor * 1000
nuevoaio$Raspberry <- nuevoaio$Raspberry * 1000

nuevoaio <- data.frame(nuevoaio, "Total" = nuevoaio$Servidor+nuevoaio$Raspberry)
plot(nuevoaio$Procesos, nuevoaio$Celery, main = "Tiempo señales cardiacas, temperatura \n y humedad (Celery)", xlab = "Procesos", ylab = "Tiempo (ms)")
plot(nuevoaio$Procesos, nuevoaio$Servidor, main = "Tiempo señales cardiacas, temperatura \n y humedad (Servidor)", xlab = "Procesos", ylab = "Tiempo (ms)")
plot(nuevoaio$Procesos, nuevoaio$Raspberry, main = "Tiempo señales cardiacas, temperatura \n y humedad (Rasberry)", xlab = "Procesos", ylab = "Tiempo (ms)")
plot(nuevoaio$Total, nuevoaio$Celery, main = "Total vs Celery (ms)", xlab = "Total", ylab = "Celery")