import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CustaddressService {
  api_link: string = "http://127.0.0.1:8000/";

  constructor(private http : HttpClient) { }

  custaddrs(data:any){ 

    return this.http.post(this.api_link + 'Customer_address_API/',data);
}}
