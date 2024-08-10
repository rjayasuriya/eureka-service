# Use the official maven/Java image to build the application
FROM maven:3.8-eclipse-temurin-17 AS build
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests

# Use the official Eclipse Temurin image to run the application
FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=build /app/target/*.jar /app/eureka-service.jar
ENTRYPOINT ["java", "-jar", "/app/eureka-service.jar"]
