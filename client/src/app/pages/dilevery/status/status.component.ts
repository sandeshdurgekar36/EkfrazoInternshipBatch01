import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-status',
  templateUrl: './status.component.html',
  styleUrls: ['./status.component.css']
})
export class StatusComponent implements OnInit {
  status!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.status!! = new FormGroup({
      'status_id':new FormControl(null, Validators.required),
      'status_name':new FormControl(null, Validators.required),
    });
  }
  get status_id() {
    return this.status!.get('status_id');
  }
  get status_name() {
    return this.status!.get('status_name');
  }

}
