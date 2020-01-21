import { INavData } from '@coreui/angular';

export const nodeItems: INavData[] = [
  {
    name: 'Master node 1',
    url: '/noeud_maitre1',
    icon: 'icon-puzzle',
    children: [
      {
        name: 'ordinary node 1',
        url: '/noeud-maitre1/noeud_ordinaire1',
        icon: 'icon-puzzle'
      },
      {
        name: 'ordinary node 2',
        url: '/noeud-maitre1/noeud_ordinaire2',
        icon: 'icon-puzzle'
      }
    ]
  },
  {
    name: 'Master node 2',
    url: '/noeud_maitre2',
    icon: 'icon-puzzle',
    children: [
      {
        name: 'ordinary node 1',
        url: '/noeud-maitre2/noeud_ordinaire1',
        icon: 'icon-puzzle'
      },
      {
        name: 'ordinary node 2',
        url: '/noeud-maitre2/noeud_ordinaire2',
        icon: 'icon-puzzle'
      }
    ]
  },
  {
    name: 'master node 3',
    url: '/noeud_maitre3',
    icon: 'icon-puzzle',
    children: [
      {
        name: 'ordinary node 1',
        url: '/noeud-maitre3/noeud_ordinaire1',
        icon: 'icon-puzzle'
      },
      {
        name: 'ordinary node 2',
        url: '/noeud-maitre3/noeud_ordinaire2',
        icon: 'icon-puzzle'
      }
    ]
  },
  {
    name: 'master node 4',
    url: '/noeud_maitre4',
    icon: 'icon-puzzle',
    children: [
      {
        name: 'ordinary node 1',
        url: '/noeud-maitre4/noeud_ordinaire1',
        icon: 'icon-puzzle'
      },
      {
        name: 'ordinary node 2',
        url: '/noeud-maitre4/noeud_ordinaire2',
        icon: 'icon-puzzle'
      }
    ]
  }
]