import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DropdetComponent } from './dropdet.component';

describe('DropdetComponent', () => {
  let component: DropdetComponent;
  let fixture: ComponentFixture<DropdetComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DropdetComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DropdetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
