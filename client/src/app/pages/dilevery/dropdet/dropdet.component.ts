import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-dropdet',
  templateUrl: './dropdet.component.html',
  styleUrls: ['./dropdet.component.css']
})
export class DropdetComponent implements OnInit {
  dropd!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.dropd! = new FormGroup({
      'Customer_address_id':new FormControl(null, Validators.required),
      'drop_data_time':new FormControl(null, Validators.required),
      'drop_date':new FormControl(null, Validators.required),
      'drop_time':new FormControl(null, Validators.required),
      'priority':new FormControl(null, Validators.required),
      'drop_id_list':new FormControl(null, Validators.required),
      
      
      
      
    });
  }
  get Customer_address_id() {
    return this.dropd!.get('Customer_address_id');
  }
  get drop_data_time() {
    return this.dropd!.get('drop_data_time');
  }
  get drop_date() {
    return this.dropd!.get('drop_date');
  }
  get drop_time() {
    return this.dropd!.get('drop_time');
  }
  get priority() {
    return this.dropd!.get('priority');
  }
  get drop_id_list() {
    return this.dropd!.get('drop_id_list');
  }
  
  

}
