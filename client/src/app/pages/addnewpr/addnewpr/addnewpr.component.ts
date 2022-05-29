import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-addnewpr',
  templateUrl: './addnewpr.component.html',
  styleUrls: ['./addnewpr.component.css']
})
export class AddnewprComponent implements OnInit {
  anewp!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.anewp! = new FormGroup({
      'vehicleTypeName':new FormControl(null, Validators.required),
      'capacity':new FormControl(null, Validators.required),
      'size':new FormControl(null, Validators.required),
      'details':new FormControl(null, Validators.required),
      'price_per_km':new FormControl(null, Validators.required),
      'min_charge':new FormControl(null, Validators.required),
      'max_time_min':new FormControl(null, Validators.required),
      'badge':new FormControl(null, Validators.required),
      
      
    });
  }
  get vehicleTypeName() {
    return this.anewp!.get('vehicleTypeName');
  }
  get capacity() {
    return this.anewp!.get('capacity');
  }
  get size() {
    return this.anewp!.get('size');
  }
  get details() {
    return this.anewp!.get('details');
  }
  get price_per_km() {
    return this.anewp!.get('price_per_km');
  }
  get min_charge() {
    return this.anewp!.get('min_charge');
  }
  get max_time_min() {
    return this.anewp!.get('max_time_min');
  }
  get badge() {
    return this.anewp!.get('badge');
  }
  


}
