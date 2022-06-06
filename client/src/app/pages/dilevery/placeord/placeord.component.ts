import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-placeord',
  templateUrl: './placeord.component.html',
  styleUrls: ['./placeord.component.css']
})
export class PlaceordComponent implements OnInit {
  plco!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.plco! = new FormGroup({
      'user_id':new FormControl(null, Validators.required),
      'pickup_id':new FormControl(null, Validators.required),
      'drop_id_list':new FormControl(null, Validators.required),
      'vehicles_type_id':new FormControl(null, Validators.required),
      'total_estimated_KM':new FormControl(null, Validators.required),
      'total_estimated_AMT':new FormControl(null, Validators.required),
      'ristrict_no_of_drop':new FormControl(null, Validators.required),
      
      
      
    });
  }
  get user_id() {
    return this.plco!.get('user_id');
  }
  get pickup_id() {
    return this.plco!.get('pickup_id');
  }
  get drop_id_list() {
    return this.plco!.get('drop_id_list');
  }
  get vehicles_type_id() {
    return this.plco!.get('vehicles_type_id');
  }
  get total_estimated_KM() {
    return this.plco!.get('total_estimated_KM');
  }
  get total_estimated_AMT() {
    return this.plco!.get('total_estimated_AMT');
  }
  get ristrict_no_of_drop() {
    return this.plco!.get('ristrict_no_of_drop');
  }
  

}
