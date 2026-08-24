FROM eclipse-temurin:21

WORKDIR /app

COPY HelloWorld.java ./
RUN javac --add-modules jdk.httpserver HelloWorld.java

CMD ["java", "HelloWorld.java"]