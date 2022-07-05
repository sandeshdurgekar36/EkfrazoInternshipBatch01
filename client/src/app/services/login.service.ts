import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class LoginService {

  api_link: string = "http://127.0.0.1:8000/";
  constructor(private http : HttpClient) { }

  logins(data:any){ 
    return this.http.post(this.api_link + 'log/',data);
  }
}
