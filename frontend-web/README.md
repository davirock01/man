# Fleet Maintenance System - Frontend Web

Frontend web application for coordinators and administrators.

## Features

- **Coordinador Dashboard**: 3-panel dashboard with predictive alerts, reactive alerts, and recurring patterns
- **Vehicle Context View**: Complete vehicle information with health score, PM predictions, and history
- **Work Order Management**: Create, assign, and track work orders
- **Admin Panel**: Manage users, vehicles, checklists, and PM policies

## Tech Stack

- React 18 with TypeScript
- Vite for build tooling
- Axios for API communication
- Zustand for state management
- React Query for data fetching
- Tailwind CSS for styling
- Recharts for data visualization

## Getting Started

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## Project Structure

```
src/
├── components/
│   ├── common/           # Shared components
│   ├── coordinador/      # Coordinator components
│   └── admin/            # Admin components
├── services/
│   └── api.ts           # API client
├── store/               # Zustand stores
├── types/               # TypeScript types
└── App.tsx             # Main app component
```

## Environment Variables

Create a `.env` file:

```
VITE_API_URL=http://localhost:8000
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
```


