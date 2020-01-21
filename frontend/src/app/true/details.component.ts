import { Component, OnInit } from '@angular/core';
import { nodeItems } from '../details/_navNode';


@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  public sidebarMinimized = false;
  public navItems = nodeItems;

  toggleMinimize(e) {
    this.sidebarMinimized = e;
  }

  numero_noeud_ordinaire = 1;

  
}
