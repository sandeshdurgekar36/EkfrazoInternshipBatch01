import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { DropdetService } from 'src/app/services/dropdet.service'; 
import { Router } from '@angular/router';



@Component({
  selector: 'app-dropdet',
  templateUrl: './dropdet.component.html',
  styleUrls: ['./dropdet.component.css']
})
export class DropdetComponent implements OnInit {
  

  constructor(private dService: DropdetService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.dropdetform = new FormGroup({
      'Customer_address_id':new FormControl(null, Validators.required),
      'drop_data_time':new FormControl(null, Validators.required),
      'drop_date':new FormControl(null, Validators.required),
      'drop_time':new FormControl(null, Validators.required),
      'priority':new FormControl(null, Validators.required),
      'drop_id_list':new FormControl(null, Validators.required),
      
      
      
      
    });
  }
  get Customer_address_id() {
    return this.dropdetform.get('Customer_address_id');
  }
  get drop_data_time() {
    return this.dropdetform.get('drop_data_time');
  }
  get drop_date() {
    return this.dropdetform.get('drop_date');
  }
  get drop_time() {
    return this.dropdetform.get('drop_time');
  }
  get priority() {
    return this.dropdetform.get('priority');
  }
  get drop_id_list() {
    return this.dropdetform.get('drop_id_list');
  }
  dropdetform = this.fb.group({

    Customer_address_id: ['',Validators.required],
    drop_data_time: ['',Validators.required],
    drop_date: ['',Validators.required],
    drop_time: ['',Validators.required],
    priority: ['',Validators.required],
    drop_id_list: ['',Validators.required],

  })
  drops(){
    console.log(this.dropdetform.value)
    this.dService.drops(this.dropdetform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}
