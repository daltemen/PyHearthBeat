solo.celery <- read.table("solo-celery.txt")
solo.server <- read.table("solo-server.txt")
solo.rasp <- read.table("solo-rasp.txt")
atipicosTsolo <- c()

procesossolo <- c(1:3474)
solo.celery <- data.frame("Procesos" = procesossolo, "Tiempo" = solo.celery$V1)
solo.server <- data.frame("Procesos" = procesossolo, "Tiempo" = solo.server$V1)
solo.rasp <- data.frame("Procesos" = procesossolo, "Tiempo" = solo.rasp$V1)

quitaratipicossolo <- function(valor){
  atipicos <- c()
  for(i in procesossolo){
    if(solo.celery$Tiempo[i] > valor)
    {atipicos <- c(atipicos, i)}
  }
  print(length(atipicos))
  atipicosTsolo <<- c(atipicosTsolo, atipicos)
}

quitaratipicossolo2 <- function(valor){
  atipicos2 <- c()
  for(i in procesossolo){
    if(solo.server$Tiempo[i] > valor)
    {atipicos2 <- c(atipicos2, i)}
  }
  print(length(atipicos2))
  atipicosTsolo <<- c(atipicosTsolo, atipicos2)
}

quitaratipicossolo3 <- function(valor){
  atipicos3 <- c()
  for(i in procesossolo){
    if(solo.rasp$Tiempo[i] > valor)
    {atipicos3 <- c(atipicos3, i)}
  }
  print(length(atipicos3))
  atipicosTsolo <<- c(atipicosTsolo, atipicos3)
}

quitaratipicossolo(0.04)
quitaratipicossolo2(0.005)
quitaratipicossolo3(0.002)
print(atipicosTsolo)


fullsolo <- data.frame("Procesos" = procesossolo, "Celery" = solo.celery$Tiempo, "Servidor" = solo.server$Tiempo, "Raspberry" = solo.rasp$Tiempo)

atipicosTsolo2 <- as.factor(atipicosTsolo)
y <- levels(atipicosTsolo2)

nuevosolo <- fullsolo[-c(as.integer(y)),]
nuevosolo$Procesos <- c(1:length(nuevosolo$Procesos))

nuevosolo$Celery <- nuevosolo$Celery * 1000
nuevosolo$Servidor <- nuevosolo$Servidor * 1000
nuevosolo$Raspberry <- nuevosolo$Raspberry * 1000

nuevosolo <- data.frame(nuevosolo, "Total" = nuevosolo$Servidor+nuevosolo$Raspberry)

plot(nuevosolo$Procesos, nuevosolo$Celery, xlab = "Procesos", ylab = "Tiempo (ms)", main = "Tiempo señales cardiacas (Celery)")
plot(nuevosolo$Procesos, nuevosolo$Servidor, xlab = "Procesos", ylab = "Tiempo (ms)", main = "Tiempo señales cardiacas (Servidor)")
plot(nuevosolo$Procesos, nuevosolo$Raspberry, xlab = "Procesos", ylab = "Tiempo (ms)", main = "Tiempo señales cardiacas (Raspberry)")
plot(nuevosolo$Total, nuevosolo$Celery, main = "Total vs Celery (ms)", xlab = "Total", ylab = "Celery")