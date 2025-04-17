import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../../services/user.service';
import { UserUpdate } from '../../models/user.model';

@Component({
  selector: 'app-edit-user',
  imports: [CommonModule, FormsModule],
  templateUrl: './edit-user.component.html',
  styleUrl: './edit-user.component.css',
})
export class EditUserComponent implements OnInit {
  user: UserUpdate = { full_name: '', username: '', email: '', password: '' };
  id!: number;

  errorMessage: string | null = null;

  constructor(
    private route: ActivatedRoute,
    private _userService: UserService,
    private router: Router
  ) {}

  // Obtener el ID del usuario desde la ruta y cargar los datos del usuario
  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    this._userService.getUserById(this.id).subscribe(
      (data) => {
        console.log('User fetched successfully:', data);
        this.errorMessage = null;
        this.user = { ...data };
      },
      (error) => {
        console.error('Error fetching user:', error);
        this.errorMessage = 'Failed to fetch user. Please try again.';
      }
    );
  }

  // Guardar los cambios del usuario
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

    this._userService.updateUser(this.id, this.user).subscribe(
      () => {
        console.log('User updated successfully');
        this.errorMessage = null;
        this.router.navigate(['/']);
      },
      (error) => {
        console.error('Error updating user:', error);
        this.errorMessage = 'Failed to update user. Please try again.';
      }
    );
  }
}
