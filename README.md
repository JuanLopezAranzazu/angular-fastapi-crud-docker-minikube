# Proyecto

## Ejecutar Solución Local con Docker

Ejecutar backend
```bash
docker-compose build backend
```

Ejecutar frontend
```bash
docker-compose build frontend
```

Ejecutar todo
```bash
docker-compose up --build
```

## Ejecutar Kubernetes con Minikube

Subir imágenes a Docker Hub
```bash
docker login
docker build -t yourusername/yourimage:latest .
docker push yourusername/yourimage:latest
```

Iniciar Minikube
```bash
minikube start
```

Aplicar los Manifiestos
```bash
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/postgres-service.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml
```

Ver estados para deployments, pods y services
```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

Acceder a la App
```bash
minikube service frontend
```