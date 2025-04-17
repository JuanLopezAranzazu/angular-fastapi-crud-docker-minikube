import { Routes } from '@angular/router';
import { ListUserComponent } from './pages/list-user/list-user.component';
import { AddUserComponent } from './pages/add-user/add-user.component';
import { EditUserComponent } from './pages/edit-user/edit-user.component';
import { MissingComponent } from './pages/missing/missing.component';

export const routes: Routes = [
  { path: '', component: ListUserComponent },
  { path: 'add-user', component: AddUserComponent },
  { path: 'edit-user/:id', component: EditUserComponent },
  { path: '**', component: MissingComponent }, // Redireccionar a una página de error 404
];
