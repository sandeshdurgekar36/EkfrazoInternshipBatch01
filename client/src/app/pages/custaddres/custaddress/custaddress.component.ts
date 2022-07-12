import { Component, OnInit } from '@angular/core';
import { CustaddressService } from 'src/app/services/custaddress.service';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { Router } from '@angular/router';




@Component({
  selector: 'app-custaddress',
  templateUrl: './custaddress.component.html',
  styleUrls: ['./custaddress.component.css']
})
export class CustaddressComponent implements OnInit {
  custaddres!: FormGroup;

  constructor(private cService: CustaddressService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.custaddresform= new FormGroup({
      'id':new FormControl(null, Validators.required),
      'House_number':new FormControl(null, Validators.required),
      'address':new FormControl(null, Validators.required),
      'city_id':new FormControl(null, Validators.required),
      'account_table_details':new FormControl(null, Validators.required),
      'account_no':new FormControl(null, Validators.required),     
    });
  }
  get id() {
    return this.custaddresform.get('id');
  }
  get House_number() {
    return this.custaddresform.get('House_number');
  }
  get address() {
    return this.custaddresform.get('address');
  }
  get city_id() {
    return this.custaddresform.get('city_id');
  }
  get account_table_details() {
    return this.custaddresform.get('account_table_details');
  }
  get account_no() {
    return this.custaddresform.get('account_no');
  }
  custaddresform = this.fb.group({
    id : ['',Validators.required],
   House_number : ['',Validators.required],
   address: ['',Validators.required],
   city_id: ['',Validators.required],
   account_table_details: ['',Validators.required],
   account_no: ['',Validators.required],

  })
  
  custaddrs(){
    console.log(this.custaddresform.value)
    this.cService.custaddrs(this.custaddresform.value).subscribe(response =>{
      alert("State Added");
      console.log(response)
    })

  }
}