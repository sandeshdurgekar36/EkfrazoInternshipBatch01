import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-custaddress',
  templateUrl: './custaddress.component.html',
  styleUrls: ['./custaddress.component.css']
})
export class CustaddressComponent implements OnInit {
  custaddres!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.custaddres! = new FormGroup({
      'id':new FormControl(null, Validators.required),
      'House_number':new FormControl(null, Validators.required),
      'address':new FormControl(null, Validators.required),
      'city_id':new FormControl(null, Validators.required),
      'account_table_details':new FormControl(null, Validators.required),
      'account_no':new FormControl(null, Validators.required),
      
      
      
      
    });
  }
  get id() {
    return this.custaddres!.get('id');
  }
  get House_number() {
    return this.custaddres!.get('House_number');
  }
  get address() {
    return this.custaddres!.get('address');
  }
  get city_id() {
    return this.custaddres!.get('city_id');
  }
  get account_table_details() {
    return this.custaddres!.get('account_table_details');
  }
  get account_no() {
    return this.custaddres!.get('account_no');
  }
  
  

}