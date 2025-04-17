import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from '../../services/user.service';
import { UserCreate } from '../../models/user.model';

@Component({
  selector: 'app-add-user',
  imports: [CommonModule, FormsModule],
  templateUrl: './add-user.component.html',
  styleUrl: './add-user.component.css',
})
export class AddUserComponent {
  user: UserCreate = {
    full_name: '',
    username: '',
    email: '',
    password: '',
  };

  errorMessage: string | null = null;

  constructor(private _userService: UserService, private router: Router) {}

  // Guardar el nuevo usuario
  save() {
    // Validar los datos del formulario
    if (
      !this.user.full_name ||
      !this.user.username ||
      !this.user.email ||
      !this.user.password
    ) {
      this.errorMessage = 'All fields are required.';
      return;
    }

    if (this.user.password.length < 6) {
      this.errorMessage = 'Password must be at least 6 characters long.';
      return;
    }

    if (!this.user.email.includes('@')) {
      this.errorMessage = 'Invalid email address.';
      return;
    }

    this._userService.createUser(this.user).subscribe(
      () => {
        console.log('User created successfully');
        this.errorMessage = null;
        this.router.navigate(['/']);
      },
      (error) => {
        console.error('Error creating user:', error);
        this.errorMessage = 'Failed to create user. Please try again.';
      }
    );
  }
}
