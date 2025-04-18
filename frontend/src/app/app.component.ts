import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { environment } from '../environments/environment';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent implements OnInit {
  title = 'frontend';

  ngOnInit() {
    // Mostrar la apiUrl en la consola al iniciar el servicio
    console.log('API URL:', environment.apiUrl);
  }
}
