// Esquema base para el usuario
export interface UserBase {
  username: string;
  email: string;
  full_name?: string;
}

// Esquema para la creación de un nuevo usuario
export interface UserCreate extends UserBase {
  password: string;
}

// Esquema para actualizar un usuario existente
export interface UserUpdate {
  username?: string;
  email?: string;
  full_name?: string;
  password?: string;
}

// Esquema para la respuesta del usuario
export interface UserResponse extends UserBase {
  id: number;
}
