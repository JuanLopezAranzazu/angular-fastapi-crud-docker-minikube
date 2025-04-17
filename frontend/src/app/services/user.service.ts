import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { UserCreate, UserUpdate, UserResponse } from '../models/user.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private apiUrl = `${environment.apiUrl}/api/v1/user`;

  constructor(private http: HttpClient) {}

  // Obtener usuarios por paginación
  getUsersByPagination(skip: number, limit: number = 10) {
    return this.http.get<UserResponse[]>(
      `${this.apiUrl}?skip=${skip}&limit=${limit}`
    );
  }

  // Obtener usuarios por búsqueda
  getUsers() {
    return this.http.get<UserResponse[]>(`${this.apiUrl}`);
  }

  // Obtener usuarios por id
  getUserById(id: number) {
    return this.http.get<UserResponse>(`${this.apiUrl}/${id}`);
  }

  // Crear usuario
  createUser(user: UserCreate) {
    return this.http.post<UserResponse>(`${this.apiUrl}`, user);
  }

  // Actualizar usuario
  updateUser(id: number, user: UserUpdate) {
    return this.http.put<UserResponse>(`${this.apiUrl}/${id}`, user);
  }

  // Eliminar usuario
  deleteUser(id: number) {
    return this.http.delete<UserResponse>(`${this.apiUrl}/${id}`);
  }
}
