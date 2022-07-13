import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class StateService {
  
  api_link: string = "localhost:8000/";
  constructor(private http : HttpClient) { }

states(data:any){ 
  return this.http.post('http://localhost:8000/StateAPI/',data);
}
}
