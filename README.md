# Spark + Kafka Streaming — Evidencia Actividad N3

## 🎯 Objetivo
Implementar un flujo de procesamiento en **Apache Spark Streaming** integrado con **Apache Kafka**, como evidencia de la actividad N3 del curso de Big Data.

## 📂 Requisitos
- Apache Spark 3.x
- Apache Kafka
- Zookeeper
- Python 3.x
- Máquina virtual Linux (Ubuntu/Debian)

## ⚙️ Pasos de ejecución
1. **Iniciar Zookeeper**
   '''bash
   bin/zookeeper-server-start.sh config/zookeeper.properties

2. **Iniciar el broker de kafka**
   '''bash
   bin/kafka-server-start.sh config/server.properties

3. **Crear el topico en Kafka**
   '''bash
   bin/kafka-topics.sh --create --topic evidenciaN3 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

4. **Ejecutar el productor**
   '''bash
   bin/kafka-console-producer.sh --topic evidenciaN3 --bootstrap-server localhost:9092

5. **Ejecutar el script en Spark**
   '''bash
   spark-submit spark_kafka_streaming.py
## Conclusion
La actividad demuestra que la integración de Apache Kafka y Apache Spark Streaming es una solución sólida para el procesamiento de datos en tiempo real. Kafka asegura la distribución confiable de mensajes y Spark los transforma de manera inmediata, validando un pipeline eficiente y escalable. Con esta práctica se evidencia dominio técnico en Big Data y se cumplen los objetivos académicos de la actividad N3, mostrando habilidades aplicables en escenarios reales de la industria.
