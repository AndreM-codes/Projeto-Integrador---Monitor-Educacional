library(shiny)
library(shinydashboard)

app_colors <- list(
  header_bg = "#2F7958",
  header_hover_bg = "#004A2F",
  header_text = "#ffffff",

  sidebar_bg = "#222d32",
  sidebar_text = "#ffffff",
  sidebar_hover_bg = "#1e282c",
  sidebar_hover_text = "#ffffff",
  sidebar_active_bg = "#004A2F",
  sidebar_active_text = "#ffffff",

  body_bg = "#EADFC3",
  page_title_text = "#222222",
  body_text = "#333333",

  box_header_bg = "#3e6e32",
  box_header_text = "#ffffff",
  box_border = "#d2d6de",
  box_bg = "#ffffff",

  button_bg = "#3e6e32",
  button_hover_bg = "#335f2a",
  button_text = "#ffffff",

  input_bg = "#ffffff",
  input_text = "#333333",
  input_border = "#d2d6de",

  table_header_bg = "#3e6e32",
  table_header_text = "#ffffff",
  table_border = "#d2d6de",
  table_row_bg = "#ffffff",
  table_alt_row_bg = "#f9f9f9",
  table_text = "#333333",

  value_box_total_bg = "#3e6e32",
  value_box_growth_bg = "#3e6e32",
  value_box_status_bg = "#3e6e32",
  value_box_text = "#ffffff",
  value_box_icon = "rgba(0, 0, 0, 0.15)",

  chart_bar = "#3e6e32",
  chart_bg = "#ffffff",
  chart_border = "#ffffff",
  chart_axis_text = "#333333",
  chart_title_text = "#222222"
)

ui <- dashboardPage(
  dashboardHeader(
    title = "Sample Dashboard"
  ),

  dashboardSidebar(
    sidebarMenu(
      id = "sidebar",
      
      menuItem("Dashboard", tabName = "dashboard", icon = icon("dashboard")),
      
      menuItem("Dashboard", tabName = "item1", icon = icon("dashboard"), startExpanded = FALSE,
               menuSubItem("Educação Infantil", tabName = "grafico1", icon = icon("1")),
               menuSubItem("Alfabetização", tabName = "grafico2", icon = icon("2")),
               menuSubItem("Ensino Fundamental", tabName = "tabela1", icon = icon("3")),
               menuSubItem("Educação Integral", tabName = "tabela1", icon = icon("4")),
               menuSubItem("Diversidade e Inclusão", tabName = "tabela1", icon = icon("5")),
               menuSubItem("Educação Profissional", tabName = "tabela1", icon = icon("6")),
               menuSubItem("Educação Superior", tabName = "tabela1", icon = icon("7")),
               menuSubItem("Estrutura da Educação", tabName = "tabela1", icon = icon("8"))
               )
      )
  ),

  dashboardBody(
    tags$head(
      tags$style(HTML(sprintf("
        .skin-blue .main-header .logo,
        .skin-blue .main-header .navbar {
          background-color: %s;
          color: %s;
        }

        .skin-blue .main-header .logo:hover {
          background-color: %s;
          color: %s;
        }

        .skin-blue .main-header .logo,
        .skin-blue .main-header .navbar .sidebar-toggle {
          color: %s;
        }

        .skin-blue .main-header .navbar .sidebar-toggle:hover {
          background-color: %s;
        }

        .content-wrapper,
        .right-side {
          background-color: %s;
          color: %s;
        }

        h1, h2, h3, h4 {
          color: %s;
        }

        .skin-blue .main-sidebar,
        .skin-blue .left-side {
          background-color: %s;
        }

        .skin-blue .sidebar-menu > li > a {
          color: %s;
        }

        .skin-blue .sidebar-menu > li:hover > a {
          background-color: %s;
          color: %s;
        }

        .skin-blue .sidebar-menu > li.active > a {
          background-color: %s;
          color: %s;
        }

        .box {
          background-color: %s;
          border-top-color: %s;
        }

        .box.box-primary {
          border-top-color: %s;
        }

        .box.box-solid.box-primary {
          border-color: %s;
        }

        .box.box-solid.box-primary > .box-header {
          background-color: %s;
          color: %s;
        }

        .btn-default,
        .btn-default:focus {
          background-color: %s;
          border-color: %s;
          color: %s;
        }

        .btn-default:hover {
          background-color: %s;
          border-color: %s;
          color: %s;
        }

        .form-control,
        .selectize-input {
          background-color: %s;
          border-color: %s;
          color: %s;
        }

        table {
          background-color: %s;
          border-color: %s;
          color: %s;
        }

        table > thead > tr > th {
          background-color: %s;
          color: %s;
          border-color: %s;
        }

        table > tbody > tr > td {
          border-color: %s;
        }

        table > tbody > tr:nth-child(odd) {
          background-color: %s;
        }

        table > tbody > tr:nth-child(even) {
          background-color: %s;
        }

        #total_box .small-box {
          background-color: %s !important;
          color: %s;
        }

        #growth_box .small-box {
          background-color: %s !important;
          color: %s;
        }

        #status_box .small-box {
          background-color: %s !important;
          color: %s;
        }

        .small-box .icon {
          color: %s;
        }
      ",
        app_colors$header_bg,
        app_colors$header_text,
        app_colors$header_hover_bg,
        app_colors$header_text,
        app_colors$header_text,
        app_colors$header_hover_bg,
        app_colors$body_bg,
        app_colors$body_text,
        app_colors$page_title_text,
        app_colors$sidebar_bg,
        app_colors$sidebar_text,
        app_colors$sidebar_hover_bg,
        app_colors$sidebar_hover_text,
        app_colors$sidebar_active_bg,
        app_colors$sidebar_active_text,
        app_colors$box_bg,
        app_colors$box_border,
        app_colors$box_border,
        app_colors$box_header_bg,
        app_colors$box_header_bg,
        app_colors$box_header_text,
        app_colors$button_bg,
        app_colors$button_bg,
        app_colors$button_text,
        app_colors$button_hover_bg,
        app_colors$button_hover_bg,
        app_colors$button_text,
        app_colors$input_bg,
        app_colors$input_border,
        app_colors$input_text,
        app_colors$table_row_bg,
        app_colors$table_border,
        app_colors$table_text,
        app_colors$table_header_bg,
        app_colors$table_header_text,
        app_colors$table_border,
        app_colors$table_border,
        app_colors$table_row_bg,
        app_colors$table_alt_row_bg,
        app_colors$value_box_total_bg,
        app_colors$value_box_text,
        app_colors$value_box_growth_bg,
        app_colors$value_box_text,
        app_colors$value_box_status_bg,
        app_colors$value_box_text,
        app_colors$value_box_icon
      )))
    ),

    tabItems(
      tabItem(
        tabName = "dashboard",
        h2("Dashboard sample"),
        fluidRow(
          valueBoxOutput("total_box"),
          valueBoxOutput("growth_box"),
          valueBoxOutput("status_box")
        ),
        fluidRow(
          box(
            title = "Sample plot",
            width = 6,
            status = "primary",
            solidHeader = TRUE,
            plotOutput("sample_plot")
          ),
          box(
            title = "Sample summary",
            width = 6,
            status = "primary",
            solidHeader = TRUE,
            tableOutput("sample_summary")
          )
        )
      ),

      tabItem(
        tabName = "data",
        h2("Data sample"),
        fluidRow(
          box(
            title = "Filters",
            width = 4,
            status = "primary",
            solidHeader = TRUE,
            selectInput(
              inputId = "category",
              label = "Category",
              choices = c("All", "A", "B", "C"),
              selected = "All"
            ),
            actionButton("refresh", "Refresh", icon = icon("refresh"))
          ),
          box(
            title = "Table",
            width = 8,
            status = "primary",
            solidHeader = TRUE,
            tableOutput("sample_table")
          )
        )
      ),

      tabItem(
        tabName = "about",
        h2("About"),
        p("This is a clean sample UI for a Shiny dashboard.")
      )
    )
  )
)
