import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { UserService } from '../../services/user.service';
import { UserResponse } from '../../models/user.model';

@Component({
  selector: 'app-list-user',
  imports: [CommonModule, RouterModule],
  templateUrl: './list-user.component.html',
  styleUrl: './list-user.component.css',
})
export class ListUserComponent implements OnInit {
  users: UserResponse[] = [];

  errorMessage: string | null = null;

  constructor(private _userService: UserService) {}

  ngOnInit(): void {
    this.loadUsers();
  }

  // Obtener la lista de usuarios
  loadUsers() {
    this._userService.getUsers().subscribe(
      (response: UserResponse[]) => {
        console.log('Users loaded:', response);
        this.errorMessage = null;
        this.users = response;
      },
      (error) => {
        console.error('Error loading users:', error);
        this.errorMessage = 'Error loading users: ' + error.message;
      }
    );
  }

  // Eliminar un usuario por ID
  deleteUser(id: number) {
    this._userService.deleteUser(id).subscribe(
      () => {
        console.log('User deleted:', id);
        this.errorMessage = null;
        this.loadUsers();
      },
      (error) => {
        console.error('Error deleting user:', error);
        this.errorMessage = 'Error deleting user: ' + error.message;
      }
    );
  }
}
